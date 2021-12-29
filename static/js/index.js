$(document).ready(function () {

    // navbar scroll
    window.addEventListener('scroll', function () {
        let scrollPosition = window.pageYOffset;
        if (scrollPosition >= 30) {
            $('.navbar').removeClass('navbar-dark')
            $('.navbar').addClass('navbar-light')
            $('.navbar').attr('style', 'background-color: white !important;')
            $('.navbar .active').css('border-bottom', '2px solid black')
        } else {
            $('.navbar').removeClass('navbar-light')
            $('.navbar').addClass('navbar-dark')
            $('.navbar').attr('style', 'background-color: tranperant !important;')
            $('.navbar .active').css('border-bottom', '2px solid white')
        }
    });

    // owl carousel
    $('.slider').owlCarousel({
        loop: true,
        margin: 20,
        nav: false,
        responsive: {
            0: {
                items: 1
            },
            600: {
                items: 1
            },
            1000: {
                items: 3
            }
        }
    });
});

(function () {
    'use strict'

    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    var forms = document.querySelectorAll('.needs-validation')

    // Loop over them and prevent submission
    Array.prototype.slice.call(forms)
        .forEach(function (form) {
            form.addEventListener('submit', function (event) {
                if (!form.checkValidity()) {
                    event.preventDefault()
                    event.stopPropagation()
                }

                form.classList.add('was-validated')
            }, false)
        })
})()
