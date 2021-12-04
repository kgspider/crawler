var e = function () {
    for (var t = arguments.length, n = Array(t), r = 0; r < t; r++)
        n[r] = arguments[r];
    var e = n.length
        , i = "string" == typeof n[e - 1] ? n[e - 1] : "Assert Error"
        , o = !0
        , u = !1
        , c = void 0;
    try {
        for (var f, a = n[Symbol.iterator](); !(o = (f = a.next()).done); o = !0) {
            if (!f.value)
                throw new Error(i)
        }
    } catch (t) {
        u = !0,
            c = t
    } finally {
        try {
            !o && a.return && a.return()
        } finally {
            if (u)
                throw c
        }
    }
}
    , i = function () {
    return Math.random() >= .5
}
    , o = function (t) {
    var n = /[A-Za-z0-9\-\_\.\!\~\*\'\(\)]/g
        , r = t.replace(n, function (t) {
        return t.codePointAt(0).toString(16)
    });
    return encodeURIComponent(r).replace(/%/g, "").toUpperCase()
}
    , u = function (t) {
    e("string" == typeof t, "utfs Error");
    var n = t.length;
    e(0 == (1 & n));
    for (var r = [], i = 0; i < n; i++)
        0 == (1 & i) && r.push("%"),
            r.push(t[i]);
    return decodeURIComponent(r.join(""))
}
    , c = function (t) {
    e("string" == typeof t);
    var n = []
        , r = !0
        , o = !1
        , u = void 0;
    try {
        for (var c, f = t[Symbol.iterator](); !(r = (c = f.next()).done); r = !0) {
            var a = c.value
                , s = Number.parseInt(a, 16);
            s < 10 ? n.push(s) : i() ? (n.push(10),
                n.push(s - 10)) : (n.push(11),
                n.push(s - 6))
        }
    } catch (t) {
        o = !0,
            u = t
    } finally {
        try {
            !r && f.return && f.return()
        } finally {
            if (o)
                throw u
        }
    }
    return n
}
    , f = function (t) {
    e(t instanceof Array);
    for (var n = [], r = t.length, i = 0; i < r;)
        t[i] < 10 ? n.push(t[i]) : 10 === t[i] ? (i++,
            n.push(t[i] + 10)) : (i++,
            n.push(t[i] + 6)),
            i++;
    return n.map(function (t) {
        return t.toString(16).toUpperCase()
    }).join("")
}
    , a = function (t) {
    return t.map(function (t) {
        return h[2 * t] + h[2 * t + 1]
    }).join("")
}
    , s = function (t) {
    var n = []
        , r = !0
        , i = !1
        , o = void 0;
    try {
        for (var c, a = t[Symbol.iterator](); !(r = (c = a.next()).done); r = !0) {
            var s = c.value
                , l = h.indexOf(s);
            -1 !== l && (1 & l || n.push(l >> 1))
        }
    } catch (t) {
        i = !0,
            o = t
    } finally {
        try {
            !r && a.return && a.return()
        } finally {
            if (i)
                throw o
        }
    }
    var v = f(n);
    e(0 == (1 & v.length));
    var p = void 0;
    try {
        p = u(v)
    } catch (t) {
        throw t
    }
    return p
}
    , h = "富强民主文明和谐自由平等公正法治爱国敬业诚信友善"

function encrypt(t) {
    return a(c(o(t)))
}

function decrypt(t) {
    return s(t)
}

// 测试样例
// console.log(encrypt("1234"))
// console.log(decrypt("和谐民主和谐文明和谐和谐和谐自由"))
