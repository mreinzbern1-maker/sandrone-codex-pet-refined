# 桑多涅 · 精绘版 Codex 桌宠

细腻 Q 版桑多涅原生桌宠，保留蓝眼睛、茶杯与茶碟，并参考角色 3D 造型修订编发盘髻、白金帽饰、蝶形束腰、前裙和袖口。

![待机预览](previews/idle.gif)

**[下载安装包 v1.0.0](downloads/Sandrone-Refined-v1.0.0.zip?raw=true)** · [完整动作](previews/all-states.gif) · [十六方向视线](previews/look-loop.gif) · [全帧图](previews/contact-sheet.png)

## 安装到 Codex

1. 安装并登录支持自定义桌宠的 Codex 桌面客户端。
2. 下载上面的 ZIP，完整解压。
3. 将解压得到的 **`sandrone-refined` 文件夹**复制到 `%USERPROFILE%\.codex\pets\`。
4. 从系统托盘完全退出 Codex，再重新打开。
5. 在 **设置 → Pets／桌宠** 中选择“桑多涅 · 精绘版”，并使用 **Show pet／显示桌宠**。也可在聊天输入 `/pet` 控制显示。

最终应当是：

```text
%USERPROFILE%\.codex\pets\sandrone-refined\pet.json
%USERPROFILE%\.codex\pets\sandrone-refined\spritesheet.png
```

macOS／Linux 用户可将同一文件夹放到 `~/.codex/pets/`；本次实际桌面验证环境为 Windows，其他平台尚未验证。若客户端版本没有自定义桌宠导入功能，需要使用支持该功能的版本。

这是原生桌宠资源包，不依赖桑多涅界面主题、调试端口或第三方启动器。安装到独立目录，不覆盖旧版 `teacup-belle`。切换回其他桌宠后，可移除此目录；如果客户端已将本地桌宠同步到账号，还需在桌宠设置中移除对应记录。

## 动作与规格

| 状态 | 帧数 | 内容 |
| --- | ---: | --- |
| idle | 6 | 待机、眨眼 |
| running-right | 8 | 向屏幕右侧移动 |
| running-left | 8 | 向屏幕左侧移动 |
| waving | 4 | 挥手 |
| jumping | 5 | 小跳与落地 |
| failed | 8 | 失败／受阻反应 |
| waiting | 6 | 等待用户／审批 |
| running | 6 | 原地专注工作 |
| review | 6 | 审视与检查 |
| look | 16 | 顺时针十六方向视线 |

- Codex v2 图集：透明 PNG，1536×2288，8 列 × 11 行，73 个有效帧。
- 每格为客户端格式要求的 **192×208**。精细化来自原稿重绘和下采样，运行时单格分辨率没有提高。
- 九组动作、透明边缘、方向与完整图集已校验；实际安装版本已在 Codex 中启用。部分相邻视线在小尺寸下变化较细微。
- [验证摘要](docs/validation.json)保留文件摘要与实际检查结果；不包含账号或本机路径。

## 获取源码与重新打包

直接编辑 `pet/sandrone-refined/` 下的资源。Python 3 标准库即可重新生成安装包：

```bash
python tools/build_release.py
```

下载包和 PNG 的 SHA256 位于 [SHA256SUMS.txt](downloads/SHA256SUMS.txt)。

## 来源与权利

原始桌宠参考：[Nayoutang/sandrone-codex-pet](https://github.com/Nayoutang/sandrone-codex-pet)。原项目说明要求在拥有相应角色美术权利的场景中分享或使用。

本版使用 AI 辅助重绘九组动作，并对生成的眼睛与脸部做逐帧方向修正。3D 模型仅用于本地观察服装与发型细节，不随包发布。角色名称和形象的权利归其原权利人，本仓库不额外授予角色或第三方美术版权许可；详见 [素材说明](ASSET-LICENSE.md)。打包脚本采用 [MIT](LICENSE-CODE)。

这是非官方同人资源，与 OpenAI、HoYoverse／COGNOSPHERE 无官方隶属关系。不要将它描述为官方授权素材。
