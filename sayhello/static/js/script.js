$(function () {
    function render_time() {
        // 这个moment时Moment.js提供的
        // $(this).data('timestamp')获取了对应元素的data-timestamp属性值
        return moment($(this).data('timestamp')).format('lll')
    }
    $('[data-toggle="tooltip"]').tooltip(
        {title: render_time}
    );
});
