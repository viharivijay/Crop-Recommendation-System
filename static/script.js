/* ==========================================================
AI Crop Recommendation System
script.js
========================================================== */

document.addEventListener("DOMContentLoaded", function () {

    console.log("Application Loaded Successfully");

    // ============================================
    // Fade-in Animation
    // ============================================

    document.body.style.opacity = "0";

    setTimeout(() => {

        document.body.style.transition = "opacity 1s";

        document.body.style.opacity = "1";

    }, 100);


    // ============================================
    // Form Validation
    // ============================================

    const form = document.querySelector("form");

    if (form) {

        form.addEventListener("submit", function (e) {

            const district = document.querySelector(
                "select[name='district']"
            );

            if (district.value === "") {

                alert("Please select a district.");

                e.preventDefault();

                return;

            }

            showLoading();

        });

    }


    // ============================================
    // Hero Image Animation
    // ============================================

    const heroImage = document.querySelector(".hero-image");

    if (heroImage) {

        heroImage.addEventListener("mouseover", function () {

            heroImage.style.transform =
                "scale(1.03)";

            heroImage.style.transition =
                ".4s";

        });

        heroImage.addEventListener("mouseleave", function () {

            heroImage.style.transform =
                "scale(1)";

        });

    }

});
