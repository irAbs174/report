function req(){
    let order_code = $(".order_code").val();
    $.ajax({
        url : '/req',
        type : 'POST',
        data : {
            'order_code': order_code,
        },
    });// end ajax
};// end fun