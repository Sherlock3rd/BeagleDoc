# 玩家进入游戏流程设计 (Login & Entry Flow Design)

本文档规划了玩家从启动游戏到正式进入游戏世界的完整交互流程，涵盖了SDK检测、网络优选、账号登录及多角色/多服务器的管理逻辑。

## 1. 整体流程图 (Overall Flowchart)

```mermaid
graph TD
    %% 全局样式定义
    classDef flowState fill:#e3f2fd,stroke:#1565c0,stroke-width:2px,color:#0d47a1;
    classDef decision fill:#fff9c4,stroke:#fbc02d,stroke-width:2px,color:#f57f17,shape:diamond;
    classDef startEnd fill:#a5d6a7,stroke:#2e7d32,stroke-width:2px,color:#1b5e20,rx:5,ry:5;
    classDef errorState fill:#ffcdd2,stroke:#c62828,stroke-width:2px,color:#b71c1c;
    classDef action fill:#ffffff,stroke:#333,stroke-width:1px,color:#333;
    classDef sceneNode fill:#e1bee7,stroke:#7b1fa2,stroke-width:2px,color:#4a148c,stroke-dasharray: 5 5;

    %% 阶段 1: 启动与检测
    subgraph Stage1_Init [1. 启动与检测]
        direction TB
        Start((游戏启动)):::startEnd --> Scene1_Launch[SCENE 1: 启动与检测]:::sceneNode
        Scene1_Launch --> NetCheck[网络环境检测]:::action
        NetCheck -->|网络异常| ErrorNet[提示网络错误/重试]:::errorState
    end

    %% 阶段 2: 账号认证
    subgraph Stage2_Login [2. 账号认证]
        direction TB
        NetCheck -->|网络良好| CheckToken{本地有 Token?}:::decision
        
        %% 自动登录路径
        CheckToken -- YES --> AutoLogin[自动/静默登录]:::action
        AutoLogin --> Auth[服务端认证]:::action
        
        %% 手动登录路径
        CheckToken -- NO --> Scene2_Login[SCENE 2: 账号登陆界面]:::sceneNode
        Scene2_Login -->|输入账号/SDK| Auth
        
        Auth -->|认证失败| Scene2_Login
    end

    %% 阶段 3: 角色决策与大厅
    subgraph Stage3_Selection [3. 角色决策与大厅]
        direction TB
        Auth -->|认证成功| CheckRole{有上次角色?}:::decision
        
        %% 路径 A: 快速开始 (老玩家)
        CheckRole -- YES --> Scene3_Lobby[SCENE 3: 登陆大厅<br/>展示上次角色]:::sceneNode
        Scene3_Lobby -->|开始游戏| EnterGameProcess[请求进入游戏]:::action
        Scene3_Lobby -->|切换/新建| Scene3_5_List[SCENE 3.5: 角色总览<br/>列表/新建]:::sceneNode
        
        %% 路径 B: 新玩家/无角色
        CheckRole -- NO --> Scene3_5_List
        
        %% 角色列表交互
        Scene3_5_List -->|选择已有角色| Scene3_Lobby
        Scene3_5_List -->|点击新建| NewGameChoice{选择世界类型?}:::decision
        
        %% 路径 C: 创建新角色
        NewGameChoice -- 合服世界 --> Scene4_Server[SCENE 4: 选择服务器]:::sceneNode
        Scene4_Server --> Scene5_SpawnRegion[SCENE 5: 出生区域]:::sceneNode
        
        NewGameChoice -- 新世界 Zone --> Scene6_PhysRegion[SCENE 6: 物理区域]:::sceneNode
        Scene6_PhysRegion --> Scene7_ZoneList[SCENE 7: Zone 列表]:::sceneNode
        Scene7_ZoneList -->|选择 Zone| EnterZone[进入 Zone]:::action
        
        Scene5_SpawnRegion --> CharacterCreation[角色定制]:::flowState
        EnterZone --> CharacterCreation
        
        CharacterCreation -->|创建完成| EnterGameProcess
    end

    %% 阶段 4: 进入游戏
    subgraph Stage4_Entry [4. 进入游戏]
        EnterGameProcess --> Scene8_Connect[SCENE 8: 连接中 Connecting]:::sceneNode
        Scene8_Connect --> Loading[场景加载 & 恢复]:::action
        Loading --> InGame((游戏中)):::startEnd
    end
```

## 2. 详细流程说明 (Detailed Steps)

### 2.1 游戏启动与检测 (Startup & Check) [SCENE 1]
*   **游戏启动**: 客户端冷启动。
*   **SDK检测**:
    *   初始化渠道SDK（如Google Play, iOS GameCenter, 第三方发行SDK）。
    *   检查是否需要强制更新（Version Check）。
*   **网络检测**:
    *   Ping 列表中的 Login Server 网关，选择延迟最低的节点。
    *   若无网络连接，弹出系统弹窗提示重试。

### 2.2 账号登陆 (Account Login) [SCENE 2]
*   **自动登录**: 若本地存有有效 Token，尝试静默登录。
*   **手动登录**: 唤起 SDK 登录窗口或输入账号密码。
*   **获取数据**: 登录成功后，从服务器拉取该账号下的**最近登录角色**、**拥有角色的服务器列表**以及**推荐服务器列表**。

### 2.3 开始游戏/切换 (Lobby & Selection)
这是玩家进入游戏前的核心决策界面。

#### A. 默认展示 (Default View) [SCENE 3]
*   **已有角色玩家**: 界面中心展示**上次登出的角色**模型、ID、等级及所在服务器名称。
    *   **主按钮**: 【开始游戏】 (Enter Game)。
    *   **辅助按钮**: 【切换/总览】 (Switch / All Roles) - 进入角色总览界面，可切换其他角色或创建新角色。
    *   **其他**: 【切换账号】 (Switch Account)。
*   **新玩家**: 直接进入角色总览界面 (默认显示新建角色引导)。

#### B. 角色总览与新建 (Role Overview & New Character) [SCENE 3.5]
*   **角色总览**: 展示该账号下的所有角色列表。
*   **新建角色**: 点击 [+] 号进入新角色创建流程，面临两个世界选择：
    1.  **Option 1 (Merged Server)**: 加入已合服的成熟世界 (Server [SCENE 4] -> Region [SCENE 5]) -> **进入角色定制**。
    2.  **Option 2 (New Zone)**: 加入未合服的新世界 (Region [SCENE 6] -> Zone [SCENE 7]) -> **进入角色定制**。

### 2.4 角色定制与进入游戏 (Character Creation & Entry)
进入游戏流程分为两条独立的逻辑通道：

*   **TRACK 1: NEW JOURNEY (新角色)**
    *   **流程**: 连接服务器 (Connect [SCENE 8]) -> 角色定制 (Customize) -> 出生在新手村 (Spawn)。
    *   **描述**: 玩家选择好服务器/Zone后，系统建立连接，进入捏脸界面，完成后出生在新手村。

*   **TRACK 2: CONTINUE JOURNEY (老角色)**
    *   **流程**: 大厅直接开始 (Start) -> 资源加载与连接 (Connect [SCENE 8]) -> 恢复至原场景 (Restore)。
    *   **描述**: 玩家在大厅点击开始游戏，系统直接连接上次下线的服务器/Zone，并恢复玩家位置。

## 3. 异常处理 (Exception Handling)

| 异常场景 | 处理逻辑 |
| :--- | :--- |
| **SDK 初始化失败** | 弹窗提示“组件初始化失败”，禁止进入下一步，提供退出或重试按钮。 |
| **网络超时** | 在登录或连接阶段超过 10s 无响应，提示“连接服务器超时，请检查网络”。 |
| **服务器维护** | 在选择服务器或点击开始游戏时，若目标服处于维护状态，弹窗显示维护公告及预计开服时间。 |
| **排队等待** | 若目标服务器负载过高，弹出排队窗口，显示当前排队位置及预计等待时间。 |
| **版本不兼容** | 登录前检测客户端版本，若低于服务器要求，强制引导至应用商店更新。 |
