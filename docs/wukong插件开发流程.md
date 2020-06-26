> 个人认为会使用到的知识点


#### 插件实现
* 插件需要继承`robot.sdk.AbstractPlugin`基类的`Plugin`类
* 沉浸式插件需要实现：`isVaild()`和`handle()`方法,用于判断用户指令是否适合插件处理和如何处理，设置`IS_IMMERSIVE`成员属性为`True`，可以根据需求实现`isValidImmersive()`、`restore()`和`pause()`，用于支持沉浸式应用中指令响应以及技能恢复。


#### 辅助模块
* robot.config 配置模块，用于处理wukong-robot的配置信息
    * get(),用于获取指定配置的值，并允许提供一个默认值
* robot.constants 用于获取wukong-robot相关目录和文件的位置信息
    * APP_PATH wukong-robot 根路径
    * DATA_PATH wukong-robot/static 路径
    * TEMP_PATH wukong-robot/temp 路径
    * getConfigPath() 获取配置文件路径
    * getData() 获取资源文件路径
* robot.logging 日志模块，用于打印日志
    * 等级
        * debug
        * info
        * error
        * critical
    * 对于stdout，level为INFO才进行打印
    * 对于文件输出，level为DEBUG才进行打印
* robot.sdk.unit 百度UNIT模块，可以用于讲用户指令解析化成结构化数据
    * getUnit() 获取解析结果
    * hasIntent() 判断意图
    * getSlots() 获取词槽
    * getSay()



