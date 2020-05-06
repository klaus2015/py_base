//针对log页面定义一个对象
var log = {
    startdt: "2019-8-5",
    enddt: "2019-9-5",
    updatedt: "2019-08-05",
    anchor: "klaus"
}
// 由对象派生业务逻辑
log.submit = {
    check: function (v) {
        //验证某个值是否为空
        var _v = (v == "")? true : false;
        return _v;
    },
    autohide:function(obj){
        //两秒之后自动隐藏这个对象
        setTimeout(function(){
            obj.hide()
        },2000)
    }
}


//定义一个验证内容是否为空的函数
function checkvalue() {

    var $username = $("#username");
    var $password = $("#password");
    var $err1 = $("#err1");
    var $err2 = $("#err2");
    //用户名和密码同时不为空的时候才可以提交
    if (!log.submit.check($username.val()) && !log.submit.check($password.val())) {

        return true;
    } else {
        //判断哪个为空,然后显示哪个错误提示信息,再返回false
        if ($username.val() == '') {
            $err1.show();
            //2秒后自动隐藏
            log.submit.autohide($err1)
            return false;
        } else {
            $err2.show();
            //2秒后自动隐藏
            log.submit.autohide($err2)
            return false;
        }
    }

}

//定义一个基于列表页的业务逻辑
var lst={
    template:function(t,u,p1,p2){
        var _html = '';
            _html += '<div class="item">';
                    
            _html += '<div class="title">';
            _html += '<h3>'+t+'</h3>';
            _html += '</div>';
        
            _html += '<div class="con">';
            
            _html += '<div class="cleft">';
            _html += '<img src="'+u+'" alt="">';
            _html += '</div>';
            
            _html += '<div class="cright">';
            _html += '<p class="ptop">';
            _html += p1;
            _html += '</p>';
            _html += '<p class="pbottom">';
            _html += p2;
            _html += '</p>';
            _html += '</div>';

            _html += '</div>';
            _html += '</div>';
        return _html;
    }
}
//定义一个数组保存数组
var arrData = [
    {
        t:"python语言的优势",
        u:"imgs/b.jpg",
        p1:"本文探讨了python语言在AI领域的优势与运用,谁会称为AI和大数据时代的第一开发语言?",
        p2:"皮皮虾 学无止境 2019-8-06 34567阅读 10001"},
    {
        t:"Web开发的优势",
        u:"imgs/b04.jpg",
        p1:"本文探讨了python语言在AI领域的优势与运用,谁会称为AI和大数据时代的第一开发语言?",
        p2:"皮皮虾 学无止境 2019-8-06 34567阅读 10009"},
    {
        t:"Javascript语言的优势",
        u:"imgs/b04.jpg",
        p1:"本文探讨了python语言在AI领域的优势与运用,谁会称为AI和大数据时代的第一开发语言?",
        p2:"皮皮虾 学无止境 2019-8-06 34567阅读 12180"
    }]
//使用流程
//1.遍历数组,获取每一项元素对象
//2.将元素获取的元素对象填充到模板中
//3.向页面元素追加模板
//通过模板生成新的列表数据
for(var i=0;i<arrData.length;i++){
    
    //通过模板生成新的列表数据
    var _HTML = lst.template(arrData[i].t,arrData[i].u,arrData[i].p1,arrData[i].p2);
    //将数据追加到列表中
    $(".lst").append(_HTML);
}
// var _HTML = lst.template()
//将数据追加到列表中
// $(".lst").append(_HTML)

//$(".lst").prepend(_HTML)

//定义一个基于我的图片页的业务逻辑
var pics={
    template:function(u,n,t){
        var _html = '';
        _html += '<div class="item">';
        _html += '<div class="imgs">';
        _html += '<img src="'+u+'" alt="">';
        _html += '<div class="tip">喜欢 | '+n+'</div>';
        _html += '</div>';
        _html += '<div class="title">';
        _html += '<h3>'+t+'</h3>';
        _html += '</div>';
        _html += '</div>';
    return _html;
    }
}
//定义一个包含三个对象内容的图片数组
var arrPics = [{
                    u:"imgs/a.jpg",
                    n:"1300",
                    t:"python基础学习总结"
                },{
                    u:"imgs/b04.jpg",
                    n:"2500",
                    t:"Sublime text3作为"
                },{
                    u:"imgs/banner01.jpg",
                    n:"3000",
                    t:"python学习网址及笔记" 
                }]
for(var i=0;i<arrPics.length;i++){
    var _HTML = pics.template(arrPics[i].u,arrPics[i].n,arrPics[i].t);
    $("#pics").append(_HTML);
}

