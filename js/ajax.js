< script src = "https://code.jquery.com/jquery-3.5.1.min.js" > < /script>  <
    script >
    $(document).ready(function() {
        $('.form-outline input[type="text"]').on("keyup input", function() {
            /* Get input value on change */
            var inputVal = $(this).val();
            var resultDropdown = $(this).siblings(".result");
            if (inputVal.length) {
                $.get("backend-search.php", { term: inputVal }).done(function(data) {
                    // Display the returned data in browser
                    resultDropdown.html(data);
                });
            } else {
                resultDropdown.empty();
            }
        });

        // Set search input value on click of result item
        $(document).on("click", ".result p", function() {
            $(this).parents(".form-outline").find('input[type="text"]').val($(this).text());
            $(this).parent(".result").empty();
        });
    }); <
/script>