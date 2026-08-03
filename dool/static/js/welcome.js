/* =====================================================
   CHEREMO PROMISED SHOP
   WELCOME PAGE JAVASCRIPT
===================================================== */

document.addEventListener("DOMContentLoaded", function () {


    /* =================================================
       IMAGE SLIDER
    ================================================= */

    const slides = document.querySelectorAll(".welcome-slide");

    let currentSlide = 0;

    function showSlide(index) {

        slides.forEach(function (slide) {
            slide.classList.remove("active");
        });

        if (slides.length > 0) {
            slides[index].classList.add("active");
        }
    }


    /*
       Start with the first image
    */

    if (slides.length > 0) {
        showSlide(0);
    }


    /*
       Change image quickly
       1.8 seconds gives it a fast promotional feel
    */

    setInterval(function () {

        if (slides.length === 0) {
            return;
        }

        currentSlide++;

        if (currentSlide >= slides.length) {
            currentSlide = 0;
        }

        showSlide(currentSlide);

    }, 1800);


    /* =================================================
       TYPING ANIMATION
    ================================================= */

    const typingElement =
        document.getElementById("typing-text");

    if (!typingElement) {
        return;
    }


    const phrases = [

        "Shop quality products with confidence.",

        "We deliver right to your doorstep. 🚚",

        "Affordable prices. Great products. 💰",

        "Simple and convenient online shopping. 🛍️",

        "Your order is just a few clicks away. ⚡",

        "From our shop to your doorstep. 📦",

        "Cheremo Promised Shop — shopping made easy."

    ];


    let phraseIndex = 0;
    let characterIndex = 0;

    let deleting = false;


    function typeText() {

        const currentPhrase =
            phrases[phraseIndex];


        /*
           Typing
        */

        if (!deleting) {

            typingElement.textContent =
                currentPhrase.substring(
                    0,
                    characterIndex + 1
                );

            characterIndex++;


            /*
               Finished typing
            */

            if (
                characterIndex ===
                currentPhrase.length
            ) {

                deleting = true;

                setTimeout(
                    typeText,
                    1800
                );

                return;
            }


            /*
               Typing speed
            */

            setTimeout(
                typeText,
                45
            );

        }


        /*
           Deleting
        */

        else {

            typingElement.textContent =
                currentPhrase.substring(
                    0,
                    characterIndex - 1
                );

            characterIndex--;


            /*
               Finished deleting
            */

            if (characterIndex === 0) {

                deleting = false;

                phraseIndex++;

                if (
                    phraseIndex >=
                    phrases.length
                ) {

                    phraseIndex = 0;

                }

                setTimeout(
                    typeText,
                    400
                );

                return;
            }


            /*
               Delete speed
            */

            setTimeout(
                typeText,
                25
            );

        }

    }


    /*
       Start typing
    */

    typeText();

});