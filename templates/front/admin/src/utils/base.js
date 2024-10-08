const base = {
    get() {
        return {
            url : "http://localhost:8080/djangokyhd2486/",
            name: "djangokyhd2486",
            // 退出到首页链接
            indexUrl: 'http://localhost:8080/front/dist/index.html'
        };
    },
    getProjectName(){
        return {
            projectName: "基于 Python 的高校学生职业推荐系统的设计与实现"
        } 
    }
}
export default base
