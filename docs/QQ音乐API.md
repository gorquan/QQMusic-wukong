#### 歌单接口
* 接口URL：https://c.y.qq.com/soso/fcgi-bin/client_music_search_songlist?remoteplace=txt.yqq.playlist&page_no=${pageNo - 1}&num_per_page=${pageSize}&query=${key}
* 接口参数：
    * query：搜索关键词
    * page_no：页码(-1)
    * num_per_page：页大小
* 请求方式：get
* 请求header：
    * Referer：https://y.qq.com
* 返回参数


#### 音乐接口
* 接口URL：http://c.y.qq.com/soso/fcgi-bin/client_search_cp
* 接口参数
    * format: json 返回json格式
    * n：页大小
    * p：页码(-1)
    * w：搜索关键词
    * cr：1
    * g_tk：5381
    * t：类型
        * 0 歌曲
        * 2 歌单
        * 7 歌词
        * 8 专辑
        * 9 歌手
        * 12 mv
* 返回参数