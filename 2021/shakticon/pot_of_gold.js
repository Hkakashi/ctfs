$(document).ready(function () {
    $("form").submit(function () {
        var usr = $("#cuser").val();
        var pswd = $("#cpass").val();
        var magic = "";

        var _0x3150 = ["", "length", "max", "charAt", "charCodeAt", "fromCharCode", "shakti"];

        function merge(_0xd4c8x2, _0xd4c8x3) {
            for (var _0xd4c8x4 = 0, _0xd4c8x5 = _0x3150[0], _0xd4c8x6 = Math[_0x3150[2]](_0xd4c8x2[_0x3150[1]], _0xd4c8x3[_0x3150[1]]); _0xd4c8x4 < _0xd4c8x6; _0xd4c8x4++) {
                _0xd4c8x5 += _0xd4c8x2[_0x3150[3]](_0xd4c8x4) || _0x3150[0];
                _0xd4c8x5 += _0xd4c8x3[_0x3150[3]](_0xd4c8x4) || _0x3150[0]
            };
            return _0xd4c8x5
        }

        function encryptXor(_0xd4c8x8) {
            var _0xd4c8x9 = _0x3150[0];
            for (var _0xd4c8x4 = 0, _0xd4c8xa = 1; _0xd4c8x4 < _0xd4c8x8[_0x3150[1]]; _0xd4c8x4++, _0xd4c8xa++) {
                if (_0xd4c8xa == _0xd4c8x8[_0x3150[1]]) {
                    _0xd4c8xa = 0
                };
                _0xd4c8x9 += String[_0x3150[5]](_0xd4c8x8[_0x3150[4]](_0xd4c8x4) ^ _0xd4c8x8[_0x3150[4]](_0xd4c8xa))
            };
            return _0xd4c8x9
        }
        if (usr[_0x3150[1]] == 5) {
            magic = btoa(encryptXor(merge(_0x3150[6], usr)))
        }

        if (usr) {
            $.redirect("/check.php", {
                p: pswd,
                u: usr
            }, "POST", "_blank");
        }
    });
});