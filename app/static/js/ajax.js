"use strict";
let Request;
(function(Request){
    const http = () => {
        if (window.XMLHttpRequest) {
            return new XMLHttpRequest();
        }
        if (window.ActiveXObject) {
            const names = [
                "Msxml2.XMLHTTP.6.0",
                "Msxml2.XMLHTTP.3.0",
                "Msxml2.XMLHTTP",
                "Microsoft.XMLHTTP"
            ];
            for(let name of names) {
                try {
                    return new ActiveXObject(name);
                } catch(e) {
                    return null;
                }
            }
        }
    }
    const promise = (method,url,options={}) => {
        return new Promise((resolve,reject) => {
            const req = http();
            const data = options.data || null;
            req.open(method,url);
            req.responseType = options.type || "json";
            req.onreadystatechange = () => {
                if (req.readyState == XMLHttpRequest.DONE) {
                    if (req.status == 200) {
                        resolve(req.response);
                    } else {
                        reject(Error(req.statusText));
                    }
                }
            };
            for(let [header,value] of options.headers) {
                req.setRequestHeader(header,value);
            }
            req.send(data);
        });
    }
    const post = (url,options) => promise("POST",url, options);
    const del  = (url, options) => promise("DELETE", url, options);
    const get  = (url,options) => promise("GET", url,options);
    const put  = (url, options) => promise("PUT", url,options);

})(Request || (Request = {}));