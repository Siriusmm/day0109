$(function () {
    var username=$('#username');
    var name_info=$('#name_info');
    username.blur(function () {
        var name=username.val();
        if(name==''){
            return;
        }
        $.ajax({
            url:'/check',
            data:{'username':name},
            type:'post',
            dataType:'json',
            async:true,
            success:function (data,status,xhr) {
                var msg=data.msg;
                console.log(msg);
                if(msg=='ok'){
                    name_info.html('用户名可用');
                    name_info.css({'color':'green','font-size':"12px"});
                }
                else{
                    name_info.html('该用户名已被使用');
                    name_info.css({'color':'red','font-size':"12px"});
                }
            },
            error:function (xhr,status,erro) {
                console.log('获取服务器响应失败');
                console.log(status);
                console.log(erro);
            }
        })
    })
})