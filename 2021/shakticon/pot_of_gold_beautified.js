'use strict';
$(document).ready(function() {
  $("form").submit(function() {
    /**
     * @param {?} username_correct
     * @param {?} username
     * @return {?}
     */
    function validate(username_correct, username) {
      /** @type {number} */
      var i = 0;
      var key = "";
      var max_length = Math["max"](username_correct["length"], username["length"]);
      for (; i < max_length; i++) {
        key = key + (username_correct["charAt"](i) || "");
        key = key + (username["charAt"](i) || "");
      }
      return key;
    }
    /**
     * @param {?} str1
     * @return {?}
     */
    function expect(str1) {
      var ret = "";
      /** @type {number} */
      var i = 0;
      /** @type {number} */
      var k = 1;
      for (; i < str1["length"]; i++, k++) {
        if (k == str1["length"]) {
          /** @type {number} */
          k = 0;
        }
        ret = ret + String["fromCharCode"](str1["charCodeAt"](i) ^ str1["charCodeAt"](k));
      }
      return ret;
    }
    var username = $("#cuser").val();
    var password = $("#cpass").val();
    /** @type {string} */
    var enc = "";
    /** @type {!Array} */
    var props = ["", "length", "max", "charAt", "charCodeAt", "fromCharCode", "shakti"];
    if (username["length"] == 5) {
      /** @type {string} */
      enc = btoa(expect(validate("shaki", username)));
    }
    if (username) {
      $.redirect("/check.php", {
        p : password,
        u : username
      }, "POST", "_blank");
    }
  });
});
