# CRAZYWATER WeChat Editor v6.0

以真实项目资料为依据的公众号编辑工作流：公开资料核查、采集表解析、全量图片理解、品牌叙事、事实审稿和 Word/HTML 交付。

## 豆包 / DeepSeek — 一个入口
1. [下载空白项目采集表（Word）](./豆包-DeepSeek使用/项目竣工公众号推文信息采集表-标准简版.docx)，填入已知资料，未知项写“待确认”。注意：仓库中的 DOCX 是简化整理版，具体填写以公司原始表格为准。
2. 打开 [公众号编辑一键复制完整版](./豆包-DeepSeek使用/CRAZYWATER公众号编辑_一键复制完整版_v5.4.txt)，复制全文到新的 AI 对话。
3. 上传填好的表、设计说明、原始图片和视频。AI 先核查公开资料，再问缺失或冲突问题；逐张分析已上传图片并确认是否已经发完。
4. **全部图片确认后，AI 必须重审和修订文章大纲、正文、图片说明与排列顺序**，不能仅沿用上传图片前的猜想。
5. 确认大纲后输出图文稿及不可发表的审稿说明。人工审查技术与客户/摄影许可后发布。

没有表格时同一指令会进入提问式，每轮最多3题。不要查找旧版的“方式一/方式二”文件。

[图文操作指南](./豆包-DeepSeek使用/使用指南.md)

## Codex / Claude Code
从 [crazywater-wechat-master/SKILL.md](./crazywater-wechat-master/SKILL.md) 开始；保留整个 `crazywater-wechat-master/modules` 和 `references` 结构。重点规则在 [RESEARCH_AND_MEDIA_PROTOCOL.md](./crazywater-wechat-master/references/RESEARCH_AND_MEDIA_PROTOCOL.md)。本仓库已更新，但用户尚未本地安装；GitHub 更新不会自动安装。

## 八篇深度案例库
[案例索引](./crazywater-wechat-master/references/HISTORICAL_CASEBOOK.md)只是入口，真正的逐篇档案位于 [references/cases](./crazywater-wechat-master/references/cases/)。Codex 会按新项目的文章目标选择、读取相应的完整分析档案，不再只根据八行概括模仿。部分历史案例仅提供了截图或局部文字，档案明确标注资料不完整；没有把原始完整公众号和图片镜像到 Public GitHub。

**案例档案内容**：已见历史图文顺序、标题和分章节叙事、图像位置、技术说明密度、值得借鉴的节奏、原稿可改善处，以及新项目适用边界。默认填写表直出、资料不全提问式，均须先公开检索（有工具且用户允许）、标记争议、逐张看图，确认全部图片后调整正文。

## 输出边界
图片和视频不得虚构；视频以 `{视频}` 独立占位。DOCX 若实际支持则提供可编辑文件；HTML 工具仅离线预览，并不等于微信公众号编辑器兼容验证或发布。未获权不得公开客户内部文件及素材。开源许可证尚未设置。
