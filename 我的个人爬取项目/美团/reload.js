iP.reload = function(jv) {
                    var jw;
                    var jx = {};
                    if (typeof jv === _$_543c[91]) {
                        jx = iO.parse(jv.split(_$_543c[146])[1])
                    } else {
                        if (typeof jv === _$_543c[2]) {
                            jx = jv
                        }
                    }
                    ;iP.sign = iJ(jx);
                    iP.cts = new Date().getTime();
                    jw = iI(iP);
                    if (Rohr_Opt.LogVal && typeof (window) !== _$_543c[0]) {
                        window[Rohr_Opt.LogVal] = encodeURIComponent(jw)
                    }
                    ;return jw
                }
                ;
if (typeof (Rohr_Opt) === _$_543c[2]) {
    iP.bindUserTrackEvent();
    Rohr_Opt.reload = iP.reload;
    Rohr_Opt.sign = iP.sign;
    Rohr_Opt.clean = iP.decrypt
}