var kuwo;

!function(e) {
	var t = {};

	function d(n) {
		if (t[n]) return t[n].exports;
		var r = t[n] = {
			i: n,
			l: !1,
			exports: {}
		};
		return e[n].call(r.exports, r, r.exports, d),
		r.l = !0,
		r.exports
	}

	d.n = function(e) {
		var n = e && e.__esModule ?
		function() {
			return e.
		default
		}:
		function() {
			return e
		};
		return d.d(n, "a", n),
		n
	},
	d.d = function(e, n, r) {
		d.o(e, n) || Object.defineProperty(e, n, {
			enumerable: !0,
			get: r
		})
	},
	d.o = function(object, e) {
		return Object.prototype.hasOwnProperty.call(object, e)
	}

    kuwo = d
}({
	109 : function(t, e, n) {
		var r, o, l = n(202),
		c = n(203),
		h = 0,
		d = 0;
		t.exports = function(t, e, n) {
			var i = e && n || 0,
			b = e || [],
			f = (t = t || {}).node || r,
			v = void 0 !== t.clockseq ? t.clockseq: o;
			if (null == f || null == v) {
				var m = l();
				null == f && (f = r = [1 | m[0], m[1], m[2], m[3], m[4], m[5]]),
				null == v && (v = o = 16383 & (m[6] << 8 | m[7]))
			}
			var y = void 0 !== t.msecs ? t.msecs: (new Date).getTime(),
			w = void 0 !== t.nsecs ? t.nsecs: d + 1,
			dt = y - h + (w - d) / 1e4;
			if (dt < 0 && void 0 === t.clockseq && (v = v + 1 & 16383), (dt < 0 || y > h) && void 0 === t.nsecs && (w = 0), w >= 1e4) throw new Error("uuid.v1(): Can't create more than 10M uuids/sec");
			h = y,
			d = w,
			o = v;
			var x = (1e4 * (268435455 & (y += 122192928e5)) + w) % 4294967296;
			b[i++] = x >>> 24 & 255,
			b[i++] = x >>> 16 & 255,
			b[i++] = x >>> 8 & 255,
			b[i++] = 255 & x;
			var _ = y / 4294967296 * 1e4 & 268435455;
			b[i++] = _ >>> 8 & 255,
			b[i++] = 255 & _,
			b[i++] = _ >>> 24 & 15 | 16,
			b[i++] = _ >>> 16 & 255,
			b[i++] = v >>> 8 | 128,
			b[i++] = 255 & v;
			for (var A = 0; A < 6; ++A) b[i + A] = f[A];
			return e || c(b)
		}
	},
	202 : function(t, e) {
		var n = "undefined" != typeof crypto && crypto.getRandomValues && crypto.getRandomValues.bind(crypto) || "undefined" != typeof msCrypto && "function" == typeof window.msCrypto.getRandomValues && msCrypto.getRandomValues.bind(msCrypto);
		if (n) {
			var r = new Uint8Array(16);
			t.exports = function() {
				return n(r),
				r
			}
		} else {
			var o = new Array(16);
			t.exports = function() {
				for (var t, i = 0; i < 16; i++) 0 == (3 & i) && (t = 4294967296 * Math.random()),
				o[i] = t >>> ((3 & i) << 3) & 255;
				return o
			}
		}
	},
	203 : function(t, e) {
		for (var n = [], i = 0; i < 256; ++i) n[i] = (i + 256).toString(16).substr(1);
		t.exports = function(t, e) {
			var i = e || 0,
			r = n;
			return [r[t[i++]], r[t[i++]], r[t[i++]], r[t[i++]], "-", r[t[i++]], r[t[i++]], "-", r[t[i++]], r[t[i++]], "-", r[t[i++]], r[t[i++]], "-", r[t[i++]], r[t[i++]], r[t[i++]], r[t[i++]], r[t[i++]], r[t[i++]]].join("")
		}
	}
})

function getReqId() {
	var l = kuwo(109),
	c = kuwo.n(l),
	r = c()()
    return r
}

// console.log(getReqId())
