"use strict";
let Request;
(function(Request){
    Request.http = () => {
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
    Request.promise = (method,url,options={}) => {
        return new Promise((resolve,reject) => {
            const req = Request.http();
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
    Request.post = (url,options) => Request.promise("POST",url, options);
    Request.delete  = (url, options) => Request.promise("DELETE", url, options);
    Request.get  = (url,options) => Request.promise("GET", url,options);
    Request.put  = (url, options) => Request.promise("PUT", url,options);

})(Request || (Request = {}));