jQuery(document).ready(function() {
    jQuery('#search').click(function() {
        sent_id = jQuery('#sent_id').val();
        alert(sent_id);
        jQuery('#tree').attr('src', './html/' + sent_id + '.conllu.html')
    });
});
