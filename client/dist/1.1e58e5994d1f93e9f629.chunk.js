webpackJsonp([1],{r5ef:function(n,l,t){"use strict";Object.defineProperty(l,"__esModule",{value:!0});var e=t("WT6e"),u=function(){},o=t("4qxJ"),c=t("qmzJ"),i=t("SYiH"),r=t("0DDR"),a=t("2MpB"),_=t("h4vs"),s=t("1Wt5"),d=t("LOqq"),p=t("uNW3"),g=t("aKv1"),h=t("A7mk"),m=t("B1h7"),O=t("vtGr"),M=t("kzt6"),f=t("Xjw4"),P=t("o0PC"),C=t("5Zt4"),b=t("fTw0"),x=t("bfOx"),v=t("tzB8"),w=t("YaPU"),y=function(){function n(n,l){this.userService=n,this.router=l}return n.prototype.ngOnInit=function(){this.reloadState()},n.prototype.reloadState=function(){var n=this;this.userService.getOrders().subscribe(function(l){n.orders$=w.a.of(l)})},n.prototype.statusStr=function(n){return 0===n?"Requested":1===n?"Booked":2===n?"Overdue":3===n?"Closed":4===n?"Extended":void 0},n.prototype.goToDocument=function(n){this.router.navigate(["/documents",n.toString()])},n.prototype.formatTitle=function(n){return n.length>49&&(n=n.substr(0,48)+"..."),n},n.prototype.extendOrder=function(n){var l=this;this.userService.setStatusForMyOrder(n,4).subscribe(function(n){l.userService.getOrders().subscribe(function(n){l.orders$=w.a.of(n),l.reloadState()})})},n}(),k=e._2({encapsulation:0,styles:[[".document-list[_ngcontent-%COMP%]{margin:50px 0}.document-list[_ngcontent-%COMP%]   .table[_ngcontent-%COMP%]   thead[_ngcontent-%COMP%]   th[_ngcontent-%COMP%]{border-top:0}.document-list[_ngcontent-%COMP%]   .search-btn[_ngcontent-%COMP%]{padding:8px 20px 8px 10px;cursor:pointer;float:right;height:34px}.document-list[_ngcontent-%COMP%]   .search-btn[_ngcontent-%COMP%]   .loupe[_ngcontent-%COMP%]{width:20px;height:20px;display:inline-block}.document-list[_ngcontent-%COMP%]   .dropdown-toggle[_ngcontent-%COMP%]{background:0 0;border:0;line-height:10px;width:50px;outline:0;position:relative}.document-list[_ngcontent-%COMP%]   .dropdown-toggle[_ngcontent-%COMP%]:after{top:8px;right:10px;position:absolute}.document-list[_ngcontent-%COMP%]   .input-group-append[_ngcontent-%COMP%]{height:34px;margin:0 10px 0 0}.document-list[_ngcontent-%COMP%]   .input-group-append[_ngcontent-%COMP%]   .dropdown[_ngcontent-%COMP%]{float:left}.document-list[_ngcontent-%COMP%]   #documentSearchProps[_ngcontent-%COMP%]{width:100px;height:20px;padding:0 27px 0 0;margin-right:15px;margin-top:8px;border-right:1px solid #dee2e6}.document-list[_ngcontent-%COMP%]   #documentSearchProps[_ngcontent-%COMP%]   .badge[_ngcontent-%COMP%]{float:right}.document-list[_ngcontent-%COMP%]   .dropdown-menu[_ngcontent-%COMP%]{right:22px!important;top:32px!important}.document-list[_ngcontent-%COMP%]   #documentSearch[_ngcontent-%COMP%]{padding-right:165px}.document-list[_ngcontent-%COMP%]   .thumb-wrap[_ngcontent-%COMP%]{width:44px;height:44px;border-radius:3px;-webkit-box-shadow:0 3px 5px #eee;box-shadow:0 3px 5px #eee;overflow:hidden}.document-list[_ngcontent-%COMP%]   .thumb-wrap[_ngcontent-%COMP%]   img[_ngcontent-%COMP%]{width:100%;height:auto}.document-list[_ngcontent-%COMP%]   .table-responsive[_ngcontent-%COMP%]{background:#fff;padding:40px}.document-list[_ngcontent-%COMP%]   .table-responsive[_ngcontent-%COMP%]   .content-center[_ngcontent-%COMP%]{font-size:14px;text-align:center}.document-list[_ngcontent-%COMP%]   .table-responsive[_ngcontent-%COMP%]   .closed[_ngcontent-%COMP%], .document-list[_ngcontent-%COMP%]   .table-responsive[_ngcontent-%COMP%]   .overdue-zero[_ngcontent-%COMP%]{color:#a0a0a0}.document-list[_ngcontent-%COMP%]   .table-responsive[_ngcontent-%COMP%]   th[_ngcontent-%COMP%]{text-align:center}.document-list[_ngcontent-%COMP%]   .table-responsive[_ngcontent-%COMP%]   tr[_ngcontent-%COMP%]{border-bottom:1px solid #dee2e6}.document-list[_ngcontent-%COMP%]   .table-responsive[_ngcontent-%COMP%]   td[_ngcontent-%COMP%]{border:none;vertical-align:center}.document-list[_ngcontent-%COMP%]   tbody[_ngcontent-%COMP%]   tr[_ngcontent-%COMP%]:first-child   td[_ngcontent-%COMP%]{border-top:none}.document-list[_ngcontent-%COMP%]   .document-authors[_ngcontent-%COMP%]{padding:0;margin-bottom:5px;color:#777}.document-list[_ngcontent-%COMP%]   .document-authors[_ngcontent-%COMP%]   .document-author[_ngcontent-%COMP%]{list-style:none;padding:0;display:block}.document-list[_ngcontent-%COMP%]   .document-link[_ngcontent-%COMP%]{display:block;color:inherit;text-decoration:none}.document-list[_ngcontent-%COMP%]   .document-title[_ngcontent-%COMP%]{width:100%;float:left;color:#7b79b7;white-space:nowrap;text-overflow:ellipsis;overflow:hidden}.document-list[_ngcontent-%COMP%]   .document-type[_ngcontent-%COMP%]{font-size:15px;color:#777}.document-list[_ngcontent-%COMP%]   .table-link[_ngcontent-%COMP%]{float:left;margin:9px;cursor:pointer;outline:0;opacity:.2;-webkit-transition:opacity .2s;transition:opacity .2s}.document-list[_ngcontent-%COMP%]   .table-link[_ngcontent-%COMP%]:hover{opacity:.5!important}.document-list[_ngcontent-%COMP%]   tr[_ngcontent-%COMP%]:hover   .table-link[_ngcontent-%COMP%]{opacity:.3}.document-list[_ngcontent-%COMP%]   .highlight[_ngcontent-%COMP%]{background-color:#ff0}.document-list[_ngcontent-%COMP%]   #orderStatus[_ngcontent-%COMP%]{width:100px;height:20px;padding:0 27px 0 0;margin-top:8px}.document-list[_ngcontent-%COMP%]   #orderStatus[_ngcontent-%COMP%]   .badge[_ngcontent-%COMP%]{float:right}.document-list[_ngcontent-%COMP%]   td[_ngcontent-%COMP%]{vertical-align:middle}.document-list[_ngcontent-%COMP%]   .dropdown-toggle[_ngcontent-%COMP%]{margin-top:0!important}.table-responsive[_ngcontent-%COMP%]{overflow-x:auto;overflow:inherit;min-width:830px}"]],data:{}});function S(n){return e._28(0,[(n()(),e._4(0,0,null,null,4,"div",[],null,null,null,null,null)),(n()(),e._26(-1,null,["\n              "])),(n()(),e._4(2,0,null,null,1,"button",[["class","btn btn-link"]],null,[[null,"click"]],function(n,l,t){var e=!0;return"click"===l&&(e=!1!==n.component.extendOrder(n.parent.context.$implicit.order_id)&&e),e},null,null)),(n()(),e._26(-1,null,["Extend"])),(n()(),e._26(-1,null,["\n            "]))],null,null)}function $(n){return e._28(0,[(n()(),e._4(0,0,null,null,1,"div",[],null,null,null,null,null)),(n()(),e._26(1,null,["\n              ","\n            "]))],null,function(n,l){n(l,1,0,l.component.statusStr(l.parent.context.$implicit.status))})}function A(n){return e._28(0,[(n()(),e._26(-1,null,["\n              "])),(n()(),e._4(1,0,null,null,1,"div",[["class","closed"]],null,null,null,null,null)),(n()(),e._26(2,null,["\n                ","\n              "])),(n()(),e._26(-1,null,["\n            "]))],null,function(n,l){n(l,2,0,l.component.statusStr(l.parent.context.$implicit.status))})}function j(n){return e._28(0,[(n()(),e._4(0,0,null,null,4,"span",[["style","color: red;"]],null,null,null,null,null)),(n()(),e._26(1,null,["\n              ",""])),(n()(),e._4(2,0,null,null,1,"b",[],null,null,null,null,null)),(n()(),e._26(-1,null,["\u20bd"])),(n()(),e._26(-1,null,["\n            "]))],null,function(n,l){n(l,1,0,l.parent.context.$implicit.overdue_sum)})}function I(n){return e._28(0,[(n()(),e._26(-1,null,["\n              "])),(n()(),e._4(1,0,null,null,1,"div",[["class","overdue-zero"]],null,null,null,null,null)),(n()(),e._26(-1,null,["\n                -\n              "])),(n()(),e._26(-1,null,["\n            "]))],null,null)}function D(n){return e._28(0,[(n()(),e._4(0,0,null,null,44,"tr",[],null,null,null,null,null)),(n()(),e._26(-1,null,["\n          "])),(n()(),e._4(2,0,null,null,6,"td",[],null,null,null,null,null)),(n()(),e._26(-1,null,["\n            "])),(n()(),e._4(4,0,null,null,3,"div",[["class","thumb-wrap"]],null,null,null,null,null)),(n()(),e._26(-1,null,["\n              "])),(n()(),e._4(6,0,null,null,0,"img",[],[[8,"src",4],[8,"alt",0]],null,null,null,null)),(n()(),e._26(-1,null,["\n            "])),(n()(),e._26(-1,null,["\n          "])),(n()(),e._26(-1,null,["\n          "])),(n()(),e._4(10,0,null,null,4,"td",[],null,null,null,null,null)),(n()(),e._26(-1,null,["\n            "])),(n()(),e._4(12,0,null,null,1,"span",[["class","document-title"]],null,[[null,"click"]],function(n,l,t){var e=!0;return"click"===l&&(e=!1!==n.component.goToDocument(n.context.$implicit.document.document_id)&&e),e},null,null)),(n()(),e._26(13,null,["",""])),(n()(),e._26(-1,null,["\n          "])),(n()(),e._26(-1,null,["\n          "])),(n()(),e._4(16,0,null,null,4,"td",[],null,null,null,null,null)),(n()(),e._26(-1,null,["\n            "])),(n()(),e.Z(16777216,null,null,1,null,S)),e._3(19,16384,null,0,f.k,[e.N,e.K],{ngIf:[0,"ngIf"]},null),(n()(),e._26(-1,null,["\n          "])),(n()(),e._26(-1,null,["\n          "])),(n()(),e._4(22,0,null,null,6,"td",[["class","content-center"]],null,null,null,null,null)),(n()(),e._26(-1,null,["\n            "])),(n()(),e.Z(16777216,null,null,1,null,$)),e._3(25,16384,null,0,f.k,[e.N,e.K],{ngIf:[0,"ngIf"],ngIfElse:[1,"ngIfElse"]},null),(n()(),e._26(-1,null,["\n            "])),(n()(),e.Z(0,[["closedStatus",2]],null,0,null,A)),(n()(),e._26(-1,null,["\n          "])),(n()(),e._26(-1,null,["\n          "])),(n()(),e._26(-1,null,["\n          "])),(n()(),e._4(31,0,null,null,1,"td",[["class","date content-center"]],null,null,null,null,null)),(n()(),e._26(32,null,["\n            ","\n          "])),(n()(),e._26(-1,null,["\n          "])),(n()(),e._4(34,0,null,null,1,"td",[["class","date content-center"]],null,null,null,null,null)),(n()(),e._26(35,null,["\n            ","\n          "])),(n()(),e._26(-1,null,["\n          "])),(n()(),e._4(37,0,null,null,6,"td",[["class","content-center"]],null,null,null,null,null)),(n()(),e._26(-1,null,["\n            "])),(n()(),e.Z(16777216,null,null,1,null,j)),e._3(40,16384,null,0,f.k,[e.N,e.K],{ngIf:[0,"ngIf"],ngIfElse:[1,"ngIfElse"]},null),(n()(),e._26(-1,null,["\n            "])),(n()(),e.Z(0,[["overdueZero",2]],null,0,null,I)),(n()(),e._26(-1,null,["\n          "])),(n()(),e._26(-1,null,["\n        "]))],function(n,l){n(l,19,0,1==l.context.$implicit.status&&!l.context.$implicit.document.is_bestseller&&l.context.$implicit.is_extendable),n(l,25,0,3!=l.context.$implicit.status,e._16(l,27)),n(l,40,0,l.context.$implicit.overdue_sum>0,e._16(l,42))},function(n,l){var t=l.component;n(l,6,0,e._7(1,"",l.context.$implicit.document.cover.substr(0,l.context.$implicit.document.cover.length-1),"1"),e._7(1,"",l.context.$implicit.document.title,"")),n(l,13,0,t.formatTitle(l.context.$implicit.document.title)),n(l,32,0,l.context.$implicit.date_accepted),n(l,35,0,l.context.$implicit.date_return)})}function T(n){return e._28(0,[e._19(0,P.a,[]),(n()(),e._4(1,0,null,null,50,"main",[["class","body"]],null,null,null,null,null)),(n()(),e._26(-1,null,["\n  "])),(n()(),e._4(3,0,null,null,47,"div",[["class","document-list col-lg-10 col-12 px-0 row mx-auto"]],null,null,null,null,null)),(n()(),e._26(-1,null,["\n    "])),(n()(),e._4(5,0,null,null,1,"app-navbar",[],null,null,null,C.b,C.a)),e._3(6,114688,null,0,b.a,[x.k],null,null),(n()(),e._26(-1,null,["\n    "])),(n()(),e._4(8,0,null,null,41,"div",[["class","table-responsive"]],null,null,null,null,null)),(n()(),e._26(-1,null,["\n      "])),(n()(),e._4(10,0,null,null,1,"p",[["class","text-muted italic mb-0"]],null,null,null,null,null)),(n()(),e._26(-1,null,["Order list:"])),(n()(),e._26(-1,null,["\n      "])),(n()(),e._4(13,0,null,null,35,"table",[["class","table"]],null,null,null,null,null)),(n()(),e._26(-1,null,["\n        "])),(n()(),e._4(15,0,null,null,24,"thead",[],null,null,null,null,null)),(n()(),e._26(-1,null,["\n        "])),(n()(),e._4(17,0,null,null,21,"tr",[],null,null,null,null,null)),(n()(),e._26(-1,null,["\n          "])),(n()(),e._4(19,0,null,null,0,"th",[["width","5%"]],null,null,null,null,null)),(n()(),e._26(-1,null,["\n          "])),(n()(),e._4(21,0,null,null,0,"th",[["width","35%"]],null,null,null,null,null)),(n()(),e._26(-1,null,[" "])),(n()(),e._26(-1,null,["\n          "])),(n()(),e._4(24,0,null,null,0,"th",[["width","5%"]],null,null,null,null,null)),(n()(),e._26(-1,null,["\n          "])),(n()(),e._4(26,0,null,null,1,"th",[["width","100px"]],null,null,null,null,null)),(n()(),e._26(-1,null,["Status"])),(n()(),e._26(-1,null,["\n          "])),(n()(),e._4(29,0,null,null,1,"th",[["width","130px"]],null,null,null,null,null)),(n()(),e._26(-1,null,["Accepted"])),(n()(),e._26(-1,null,[" "])),(n()(),e._26(-1,null,["\n          "])),(n()(),e._4(33,0,null,null,1,"th",[["width","130px"]],null,null,null,null,null)),(n()(),e._26(-1,null,["Return"])),(n()(),e._26(-1,null,["\n          "])),(n()(),e._4(36,0,null,null,1,"th",[["width","80px"]],null,null,null,null,null)),(n()(),e._26(-1,null,["Overdue"])),(n()(),e._26(-1,null,["\n        "])),(n()(),e._26(-1,null,["\n        "])),(n()(),e._26(-1,null,["\n        "])),(n()(),e._4(41,0,null,null,6,"tbody",[["id","searchResults"]],null,null,null,null,null)),(n()(),e._26(-1,null,["\n        "])),(n()(),e.Z(16777216,null,null,3,null,D)),e._3(44,802816,null,0,f.j,[e.N,e.K,e.q],{ngForOf:[0,"ngForOf"]},null),e._19(131072,f.b,[e.h]),e._21(46,1),(n()(),e._26(-1,null,["\n        "])),(n()(),e._26(-1,null,["\n      "])),(n()(),e._26(-1,null,["\n    "])),(n()(),e._26(-1,null,["\n  "])),(n()(),e._26(-1,null,["\n"])),(n()(),e._26(-1,null,["\n"]))],function(n,l){var t=l.component;n(l,6,0),n(l,44,0,e._27(l,44,0,n(l,46,0,e._16(l,0),e._27(l,44,0,e._16(l,45).transform(t.orders$)))))},null)}var E=e._0("app-orders",y,function(n){return e._28(0,[(n()(),e._4(0,0,null,null,1,"app-orders",[],null,null,null,T,k)),e._3(1,114688,null,0,y,[v.a,x.k],null,null)],function(n,l){n(l,1,0)},null)},{},{},[]),q=t("6txq"),K=t("SPKT"),R=t("7DMc"),Z=t("3kwk"),N=t("CXHW"),z=t("fAE3"),U=t("pv6e"),X=t("/1Uf"),B=t("8AXl"),H=t("rIqD"),W=t("HY4u"),F=t("TToO"),G=function(){function n(n,l,t){var e=this;this.actions$=n,this.userService=l,this.userActions=t,this.GetUserOrders$=this.actions$.ofType(W.a.GET_USER_ORDERS).switchMap(function(){return e.userService.getOrders()}).filter(function(n){return n.length>0}).map(function(n){return e.userActions.getUserOrdersSuccess(n)}),this.AddNewOrder$=this.actions$.ofType(W.a.ADD_NEW_ORDER).switchMap(function(n){return e.userService.bookTheDocument(n.payload)}).map(function(n){return e.userActions.addNewOrderSuccess(n)})}return Object(F.b)([Object(B.b)(),Object(F.d)("design:type",w.a)],n.prototype,"GetUserOrders$",void 0),Object(F.b)([Object(B.b)(),Object(F.d)("design:type",Object)],n.prototype,"AddNewOrder$",void 0),n}(),J=t("dyjq"),Y=t("rXch"),Q=t("eCJc"),L=t("RX2M"),V=t("F+yc"),nn=t("/I96"),ln=t("vfkA"),tn=t("qsK9"),en=t("MSQt"),un=t("UyZi"),on=t("Ep2y"),cn=t("WKBe"),rn=t("1Z2I"),an=t("A8b0"),_n=t("as+d"),sn=t("62nT"),dn=t("yDyO"),pn=t("K/oD"),gn=t("kzcK"),hn=t("DX+K"),mn=t("YHl+"),On=t("ZQSA"),Mn=t("OjCH"),fn=t("Apu7"),Pn=t("jkKh"),Cn=t("bUIH"),bn=t("xA6g"),xn=t("IgB2"),vn=t("330S");t.d(l,"UserModuleNgFactory",function(){return wn});var wn=e._1(u,[],function(n){return e._12([e._13(512,e.j,e.X,[[8,[o.a,c.a,i.a,r.a,a.a,_.a,s.a,d.a,p.a,g.a,h.a,m.a,O.a,M.a,E]],[3,e.j],e.v]),e._13(4608,f.m,f.l,[e.s,[2,f.s]]),e._13(4608,q.c,q.a,[]),e._13(5120,q.b,q.d,[q.c,e.z]),e._13(4608,K.a,K.a,[]),e._13(4608,R.d,R.d,[]),e._13(4608,R.s,R.s,[]),e._13(4608,Z.a,Z.a,[e.j,e.p,N.a]),e._13(512,f.c,f.c,[]),e._13(512,z.a,z.a,[]),e._13(512,R.q,R.q,[]),e._13(512,R.n,R.n,[]),e._13(512,U.a,U.a,[]),e._13(512,X.a,X.a,[B.a,H.a,U.a]),e._13(512,W.a,W.a,[]),e._13(512,G,G,[B.a,v.a,W.a]),e._13(1024,B.h,function(n,l){return[B.d(n),B.d(l)]},[X.a,G]),e._13(512,B.f,B.f,[B.e,B.h,[2,J.o],[2,J.n]]),e._13(512,Y.a,Y.a,[]),e._13(512,Q.a,Q.a,[]),e._13(512,L.a,L.a,[]),e._13(512,V.a,V.a,[]),e._13(512,nn.a,nn.a,[]),e._13(512,ln.a,ln.a,[]),e._13(512,R.g,R.g,[]),e._13(512,tn.a,tn.a,[]),e._13(512,en.a,en.a,[]),e._13(512,un.a,un.a,[]),e._13(512,on.a,on.a,[]),e._13(512,cn.a,cn.a,[]),e._13(512,rn.a,rn.a,[]),e._13(512,an.a,an.a,[]),e._13(512,_n.a,_n.a,[]),e._13(512,sn.a,sn.a,[]),e._13(512,dn.a,dn.a,[]),e._13(512,pn.a,pn.a,[]),e._13(512,gn.a,gn.a,[]),e._13(512,x.o,x.o,[[2,x.t],[2,x.k]]),e._13(512,hn.a,hn.a,[]),e._13(512,u,u,[]),e._13(1024,x.i,function(){return[[{path:"librarian",canActivate:[mn.a],data:{expectedRole:310},children:[{path:"",component:On.a},{path:"user-list",component:Mn.a},{path:"user/:id",children:[{path:"edit",component:fn.a},{path:"",component:Pn.a}]},{path:"document-list",children:[{path:"add",component:Cn.a},{path:"",component:bn.a}]},{path:"order-list",component:xn.a},{path:"tag-list",component:bn.a}]}],[{path:"",canActivate:[vn.a],children:[{path:"profile",children:[{path:"",component:Pn.a},{path:"edit",component:fn.a}]},{path:"orders",children:[{path:"",component:y}]}]}]]},[])])})}});