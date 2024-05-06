$(document).ready(function() {
  const regions = [
  "California"
  ]
  const popularItems= [
      {
          "id": 3,
          "title": "Milling <br> Cabernet Franc",
          "winemaker": "Robert Lawrence",
          "vintage": 2019,
          "color": "red",
          "region": "France",
          "body": "medium",
          "tannin": "medium",
          "acid": "light",
          "tasting_notes": ["grass", "stone fruit", "blackberry", "bell pepper", "graphite", "a hint of tobacco"],
          "rating": 10,
          "other_regions": ["California", "Italy", "Australia", "South Africa"],
          "description": "Crafted by the renowned Robert Chivoley, 'Milling Cabernet Franc' is a distinguished red wine that "
                         +"embodies the rich terroir of France. With a medium body, medium tannins, and light acidity, it presents a "
                         +"unique tasting profile of grass and stone fruit, indicative of its meticulous cultivation and production "
                         +"processes. This wine not only pays homage to its French origins through its complex flavors but also through "
                         +"its elegantly designed label that reflects both tradition and modernity. Rated 9.1, it stands as a testament "
                         +"to the craftsmanship and heritage of French winemaking, appealing to connoisseurs worldwide.",
          "image_url": "/static/images/milling.webp"
      },
      {
              "id": 0,
              "title": "Flowers <br> Pinot Noir",
              "winemaker": "Matt Barlowe",
              "vintage": 2012,
              "color": "red",
              "region": "Oregon",
              "body": "light",
              "tannin": "light",
              "acid": "medium",
              "tasting_notes": ["dark cherry", "floral", "raspberry", "hint of oak", "earthy undertones", "spice"],
              "rating": 9,
              "other_regions": ["California", "France", "New Zealand", "Chile", "Australia"],
              "description": "Flowers Pinot Noir by Robert Cassette stands out as a quintessential example of the elegance and complexity "
                             +"Pinot Noir can achieve, particularly from Oregon. This wine showcases a light body with light tannins and medium "
                             +"acidity, creating a harmonious balance on the palate. The initial dark cherry and floral notes are complemented "
                             +"by layers of raspberry, a hint of oak, earthy undertones, and a touch of spice, offering a nuanced tasting "
                             +"experience. Revered for its versatility and sophistication, it has rightly earned a rating of 8.7, appealing to "
                             +"both connoisseurs and casual enthusiasts alike.",
              "image_url": "/static/images/flowers.jpg"
          },
      {
          "id": 8,
          "title": "Orange Valley <br> Chardonnay",
          "vintage": 2023,
          "winemaker": "Kaci Lynne",
          "color": "white",
          "region": "California",
          "body": "light",
          "tannin": "light",
          "acid": "Medium",
          "tasting_notes": ["orange blossom", "lemon", "peach", "melon", "subtle minerality"],
          "rating": 9.1,
          "other_regions": ["France", "New York", "Washington"],
          "description": "Orange Valley Chardonnay by Kaci Lynne captures the essence of a Californian summer with its light "
                         +"and refreshing profile. Featuring light tannins and medium acidity, it delivers a delightful blend of "
                         +"orange blossom, lemon, peach, and melon, with a hint of minerality. Rated at 9.1, this Chardonnay celebrates "
                         +"the vibrant viticulture of California, melding traditional winemaking with a modern twist to enchant wine "
                         +"enthusiasts. Its label, reflecting the sunny valleys and aromatic freshness, invites a taste of California's "
                         +"finest.",
          "image_url": "/static/images/orange-valley.webp"
      }
  ];

  const container = document.getElementById('popular-items');

  if(container){
    popularItems.forEach(item => {
        const itemElement = document.createElement('div');
        itemElement.className = 'item';
        itemElement.innerHTML = `
            <div class="row">
            <div class="col-md-6">
            <a href="/view/${item.id}">
            <img alt="Photo of ${item.winemaker}'s wine from ${item.region}" class="side-img" src=${item.image_url}>
            </a>
            </div>
            <div class="col-md-6">
            <div class="popular-item-detail">
            <h6 id="wine-title">${item.title}</h6>
            <p class="light-grey">${item.winemaker}</p>
            <p class="info-purple">${getStarsHTML(item.rating)}</p>
            </div>
            </div>
        `;
        container.appendChild(itemElement);
    });
 }

  var rating = $('#itemRating').data('rating');
     if (rating !== undefined) {
         displayStarRating(rating);
     }

 function displayStarRating(rating) {
     const starHTML = getStarsHTML(rating);
     document.getElementById('starRating').innerHTML = starHTML;
 }

 function getStarsHTML(rating) {
     let starsHTML = '';
     const fullStars = Math.floor(rating / 2);
     const halfStar = rating % 2 >= 1 ? 1 : 0;
     const emptyStars = 5 - fullStars - halfStar;

     for (let i = 0; i < fullStars; i++) {
         starsHTML += '&#9733;';
     }
     if (halfStar) {
         starsHTML += '&#189;';
     }
     for (let i = 0; i < emptyStars; i++) {
         starsHTML += '&#9734;';
     }

     return starsHTML;
 }

  $('search-form').submit(function(event) {
    event.preventDefault();
    var searchQuery = $(this).find('input[name="query"]').val().trim();
    if(searchQuery === '') {
      $(this).find('input[name="query"]').val('');
      $(this).find('input[name="query"]').focus();
    } else {
      window.location.href = '/search?query=' + encodeURIComponent(searchQuery);
    }
  });

$('#add-form').submit(function(event) {
    event.preventDefault();
    var isValid = true;
    var fields = ['#color', '#body', '#tannin', '#acid'];

    fields.forEach(function(field) {
        if ($(field).val() === '') {
            isValid = false;
            $(field).addClass('inval');
        } else {
            $(field).removeClass('inval');
        }
    });

    if (!isValid) {
        $('#form-error-message').show();
    } else {
        $('#form-error-message').hide();
        var formData = $(this).serialize();

        $.ajax({
            type: "POST",
            url: "/add",
            data: formData,
            success: function(response) {
                $('#success-message').html("New item successfully created. <a class='info-purple' href='/view/" + response.itemId + "'>See it here</a>");
                $('#success-message').show();
                $('#add-form').trigger("reset");
                $('#title').focus();
            },
            error: function() {
                alert("There was a problem with the submission. Please try again.");
            }
        });
    }
});

    $('#discard-changes').on('click', function() {
        $('#popup-container').css('display', 'flex');
    });

    $('#confirm-discard').on('click', function() {
        var itemId = $(this).attr('data-item-id');
        window.location.href = '/view/' + itemId;
    });

    $('#cancel-discard').on('click', function() {
        $('#popup-container').css('display', 'none');
    });

});

