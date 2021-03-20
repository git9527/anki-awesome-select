# Anki的选择题模板

## 更新日志:
v2.0:
1. 加入多选题模式，同时兼容单选/多选
2. 添加notes字段，在显示答案后出现

v1.5: 
1. 修复iOS上Anki记忆卡软件的标签显示问题
2. 修复显示答案前不能修改的问题

## 判断说明
单选/多选情况下，标示正确/错误的所有情况如下：
### 单选
|       | 正确选项 | 错误选项 |
| :---: | :----: | :----: |
| 选中   |   ✅   |  ❌    |
| 未选中 |    ✅   | 无变化  |

### 多选
|       | 正确选项 | 错误选项 |
| :---: | :----: | :----: |
| 选中   |   ✅   |  ❌    |
| 未选中 |    ❌   | 无变化  |

## 模板字段
![image](screens/fields.png)
1. id: 推荐用逐渐增加的数字，以便后续更新卡片时作为唯一性判断依据
2. question: 问题的题干部分，需要包含扣掉的{{c1::答案}}
3. options: 可选项，中间用`||`分开
4. answer: 正确答案的序号，1为第一个，2为第二个……以此类推。若为多选题，答案之间用`||`分开
5. notes: 显示答案后的解析，非必填字段

## 各平台截图
|平台             | 单选 | 多选 |
|:--------------:|:----:|:----:|
|Mac             | ![Anki-Mac-Single](screens/1-mac-single.png) | ![Anki-Mac-Multi](screens/1-mac-multi.png) |
|Windows         | ![Anki-Windows-Single](screens/2-windows-single.png) | ![Anki-Windows-Multi](screens/2-windows-multi.png) |
|Ubuntu          | ![Anki-Ubuntu-Single](screens/3-ubuntu-single.png) | ![Anki-Ubuntu-Multi](screens/3-ubuntu-multi.png) |
|Web             | ![Anki-Web-Single](screens/4-web-single.png) | ![Anki-Web-Multi](screens/4-web-multi.png) |
|Android         | ![Anki-Android-Single](screens/5-android-single.png) | ![Anki-Android-Multi](screens/5-android-multi.png) |
|iOS - AnkiMobile| ![Anki-iOS-Mobile-Single](screens/6-ios-mobile-single.png) | ![Anki-iOS-Mobile-Multi](screens/6-ios-mobile-multi.png) |
|iOS - Anki记忆卡 | ![Anki-iOS-Card-Single](screens/7-ios-card-single.png) | ![Anki-iOS-Card-Multi](screens/7-ios-card-multi.png) |





