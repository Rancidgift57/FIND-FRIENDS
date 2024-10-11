// Check if jQuery is loaded
if (typeof jQuery === 'undefined') {
  console.error('jQuery is not loaded. Please include jQuery before this script.');
} else {
  // jQuery is loaded, proceed with your code
  $(document).ready(function() {
    $('#Send1').click(function() {
      sendFriendRequest('/send-emails');
    });

    $('#Send2').click(function() {
      sendFriendRequest('/send-emailsw');  // Assuming this is a typo, correct it as needed
    });

    $('#Send3').click(function() {
      sendFriendRequest('/send-emailsr');
    });

    function sendFriendRequest(url) {
      $.ajax({
        url: url,
        type: 'GET',
        success: function(response) {
          alert(response); // Show success message
        },
        error: function(xhr, status, error) {
          console.error('Error:', error);
          alert('Error sending friend request. Please try again.');
        }
      });
    }
  });

  // Define the loadValuesFromFiles function
  function loadValuesFromFiles(filename1) {
    loadValuesFromFile(filename1, '.person > div', populateDivs);
  }

  function loadValuesFromFile(filename, selector, callback) {
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
      if (xhr.readyState === XMLHttpRequest.DONE) {
        if (xhr.status === 200) {
          var values = xhr.responseText.split('\n');
          callback(values, selector);
        } else {
          console.error('Failed to load file: ' + filename);
        }
      }
    };
    xhr.open('GET', filename, true);
    xhr.send();
  }

  function populateDivs(values, selector) {
    var matchDivs = document.querySelectorAll(selector);
    if (!matchDivs) return;

    for (var i = 0; i < values.length; i++) {
      var value = values[i].trim();
      if (value !== '') {
        matchDivs[i].textContent = value;
      }
    }
  }

  // Run this function when the window is fully loaded
  window.onload = function() {
    loadValuesFromFiles('FINDFRIENDS3.txt');
  };
}
