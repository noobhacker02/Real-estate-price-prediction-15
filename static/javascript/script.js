function getLiftValue() {
    var uiLift = document.getElementsByName("uiLift");
    for (var i in uiLift) {
      if (uiLift[i].checked) {
        return parseInt(i) + 1;
      }
    }
    return -1; // Invalid Value
  }

  function getParkValue() {
    var uiPark = document.getElementsByName("uiPark");
    for (var i in uiPark) {
      if (uiPark[i].checked) {
        return parseInt(i) + 1;
      }
    }
    return -1; // Invalid Value
  }
  
  function getBHKValue() {
    var uiBHK = document.getElementsByName("uiBHK");
    for (var i in uiBHK) {
      if (uiBHK[i].checked) {
        return parseInt(i) + 1;
      }
    }
    return -1; // Invalid Value
  }
  
  function onClickedEstimatePrice() {
    var Area = document.getElementById("uiSqft");
    var bhk = getBHKValue();
    var Lift = getLiftValue();
    var Parking = getParkValue();
    var Location = document.getElementById("uiLocations");
    var estPrice = document.getElementById("uiEstimatedPrice");
  
    var url = "http://127.0.0.1:5000/predict_home_price";
    //   var url = "/api/predict_home_price"; // only Deployment
  
    $.post(
      url,
      {
        Location: Location.value,
        Area: Area.value,
        bhk: bhk,
        Lift: Lift,
        Parking: Parking
      },
      function (data, status) {
        estPrice.innerHTML = "<h2>" + data.estimated_price.toString() + " </h2>";
      }
    );
  }
  
  function onPageLoad() {
    var url = "http://127.0.0.1:5000/get_location_names";

    $.get(url, function (data, status) {
   
      if (data) {
        var Locations = data.Locations;
        var uiLocations = document.getElementById("uiLocations");
        $("#uiLocations").empty();
        for (var i in Locations) {
          var opt = new Option(Locations[i]); 
          $("#uiLocations").append(opt);
        }
      }
    });
  }
  
  window.onload = onPageLoad;