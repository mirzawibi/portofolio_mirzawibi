/*!
 * Halte Menuju Dunia Saya — animasi pembuka portofolio (8 detik, canvas 2D, tanpa dependensi)
 * Pakai: <link rel="stylesheet" href="halte-intro.css"> + <script src="halte-intro.js" data-auto></script>
 * Atau manual: HalteIntro.init({ ...opsi }). Lihat README.md.
 */
(function(){'use strict';

const C=document.createElement('canvas');let x=C.getContext('2d');const MAIN=x;C.width=1280;C.height=720;
const K={hb:'#14211C',red:'#EF4444',amb:'#F5A524',gld:'#FEF08A',tx:'#F0F4F1',blu:'#2F86C9',apl:'#A7C66A'},INK='#2B2540',DK='#2A2540',GLS='#A9D8F0';let SW=3,LOW=false,BUSLABEL='ST-05 · PORTOFOLIO',DECAL='URBAN TRANSIT · PWK ITS';
const cl=(v,a=0,b=1)=>Math.min(b,Math.max(a,v)),sm=u=>u*u*(3-2*u),seg=(t,a,b)=>cl((t-a)/(b-a));
const eo=u=>1-Math.pow(1-u,3),eio=u=>u<.5?4*u*u*u:1-Math.pow(-2*u+2,3)/2;
const hh=(a,b)=>((Math.sin(a*127.1+b*311.7)*43758.5453)%1+1)%1;
const rgba=(h,a)=>{const n=parseInt(h.slice(1),16);return`rgba(${n>>16},${n>>8&255},${n&255},${a})`};
/* Skala: 1 meter = mp(y) piksel pada titik tanah y; cakrawala di y=400 */
const YH=400,mp=y=>(y-YH)*.3,sw0=m=>Math.max(1.2,Math.min(3,m*.05))/m;
function R(a,b,w,h,r,f,s){x.beginPath();x.roundRect(a,b,w,h,Math.max(0,Math.min(r,Math.abs(w)/2,Math.abs(h)/2)));if(f){x.fillStyle=f;x.fill()}if(s){x.strokeStyle=INK;x.lineWidth=SW*s;x.stroke()}}
function O(a,b,r,f,s){x.beginPath();x.arc(a,b,r,0,7);x.fillStyle=f;x.fill();if(s){x.strokeStyle=INK;x.lineWidth=SW*s;x.stroke()}}
function E(a,b,rx,ry,f){x.beginPath();x.ellipse(a,b,rx,ry,0,0,7);x.fillStyle=f;x.fill()}
function GL(cx,cy,r,col,a){const g=x.createRadialGradient(cx,cy,0,cx,cy,r);g.addColorStop(0,rgba(col,1));g.addColorStop(1,rgba(col,0));x.globalAlpha=a;x.fillStyle=g;x.fillRect(cx-r,cy-r,2*r,2*r);x.globalAlpha=1}
function beam(px,py,len,a){const g=x.createLinearGradient(px,0,px-len,0);g.addColorStop(0,rgba('#FFF3B0',a));g.addColorStop(1,rgba('#FFF3B0',0));x.fillStyle=g;x.beginPath();x.moveTo(px,py);x.lineTo(px-len,py-len*.14);x.lineTo(px-len,py+len*.2);x.fill()}
function TXT(s,a,b,sz,f,st){x.font='800 '+sz+'px Trebuchet MS,sans-serif';x.textAlign='center';if(st){x.lineJoin='round';x.lineWidth=6;x.strokeStyle=INK;x.strokeText(s,a,b)}x.fillStyle=f;x.fillText(s,a,b)}
function U(a,b,m,fn){x.save();x.translate(a,b);x.scale(m,m);SW=sw0(m);fn();x.restore();SW=3}
const CC=['#EF4444','#F5A524','#F4F1EA','#2F86C9','#FFD23F','#E86F9A','#5BC0BE','#8E7CC3'],SKN=['#E8B48F','#C99A76','#8D5A3B','#F0C8A0'];
/* ===== MOBIL (meter, bagian depan di x=0) ===== */
const VT=[{L:4.5,r:.33,em:[4.47,-.32]},{L:3.8,r:.31,em:[3.77,-.32]},{L:4.6,r:.37,em:[4.57,-.35]},{L:4.5,r:.33,em:[4.47,-.32]},{L:4.3,r:.35,em:[4.27,-.35]},{L:5.1,r:.37,em:[5.07,-.35]},{L:6.2,r:.5,em:[1.91,-3.7]}];
const VS=['#9A9AA6','#9A9AA6','#8A8A96','#9A9AA6','#34323F','#6B6B78','#2A2833'],VA=[.5,.5,.52,.5,.85,.68,.95];
function dh(a,b,p){x.globalAlpha=p?.55:.8;O(a,b,.11,'#3A3050');R(a-.11,b+.09,.22,.22,.08,'#3A3050');x.globalAlpha=1}
function wh(wx,r,sp){O(wx,-r,r*1.12,DK);O(wx,-r,r,INK);O(wx,-r,r*.52,'#D7DCE4');x.strokeStyle=INK;x.lineWidth=SW*.7;for(let k=0;k<3;k++){const a=sp+k*1.047;x.beginPath();x.moveTo(wx+Math.cos(a)*r*.48,-r+Math.sin(a)*r*.48);x.lineTo(wx-Math.cos(a)*r*.48,-r-Math.sin(a)*r*.48);x.stroke()}O(wx,-r,r*.12,INK)}
function car(a,gy,m,c,ty,brake,dir,sp,lit,pitch,hz){const T=VT[ty],L=T.L,r=T.r;x.save();x.translate(dir<0?a:a+L*m,gy);x.scale(dir<0?m:-m,m);SW=sw0(m);
 E(L/2,0,L*.58,.26,'rgba(43,37,64,.3)');if(lit)beam(0,-.85,4.5,.3);
 x.translate(L/2,0);x.rotate(pitch);x.translate(-L/2,0);
 if(ty==0||ty==3){R(L*.2,-1.65,L*.5,.7,.3,c,1);R(L*.235,-1.56,L*.43,.5,.14,GLS);R(L*.44,-1.56,.06,.5,0,c);dh(L*.34,-1.3);dh(L*.58,-1.32,1);R(0,-1.12,L,.8,.36,c,1);
  if(ty==3){R(L*.42,-1.88,.6,.22,.05,'#fff',.8);R(L*.42,-1.88,.6,.07,.03,K.red);for(let k=0;k<6;k++)R(L*.1+k*.28,-.84,.14,.14,0,k%2?DK:'#fff')}}
 else if(ty==1){R(L*.16,-1.72,L*.66,.78,.3,c,1);R(L*.2,-1.63,L*.56,.58,.14,GLS);R(L*.5,-1.63,.06,.58,0,c);dh(L*.33,-1.34);dh(L*.62,-1.34,1);R(0,-1.1,L,.78,.34,c,1)}
 else if(ty==2){R(L*.12,-1.98,L*.78,.8,.26,c,1);R(L*.16,-1.88,L*.7,.58,.12,GLS);R(L*.46,-1.88,.06,.58,0,c);dh(L*.3,-1.52);dh(L*.56,-1.52,1);dh(L*.74,-1.52,1);R(L*.14,-2.07,L*.72,.07,.03,DK);R(0,-1.3,L,.98,.3,c,1);R(0,-.62,L,.22,.1,DK)}
 else if(ty==4){R(0,-2.08,L,1.76,.28,c,1);R(.14,-1.94,.8,.8,.1,GLS);R(1.15,-1.94,L-1.4,.8,.1,GLS);[1.5,2.3,3.1].forEach(h=>dh(h,-1.62,1));R(0,-1.0,L,.2,0,'#fff');R(0,-.78,L,.1,0,K.red);R(L*.25,-2.4,1.5,.32,.1,'#8B5A3C',1);R(L-.3,-1.9,.3,1.1,.05,'#6B6F7E',.7)}
 else if(ty==5){R(0,-1.12,L,.8,.3,c,1);R(.1,-1.82,1.7,.76,.25,c,1);R(.2,-1.72,1.45,.56,.12,GLS);dh(.8,-1.42);R(1.95,-1.42,L-1.95,.32,.05,DK,1);R(2.2,-2.02,.8,.62,.06,'#C48A4A',1);R(3.1,-1.88,.75,.48,.06,'#E8B84A',1);R(3.95,-1.8,.8,.4,.16,'#E8DCC4',1)}
 else{R(0,-2.62,1.8,2.3,.3,c,1);R(.12,-2.48,1.35,.95,.1,GLS);dh(.7,-1.98);R(2.0,-3.25,L-2.0,2.9,.15,'#F4F1EA',1);R(2.0,-2.1,L-2.0,.32,0,c);R(2.0,-1.7,L-2.0,.1,0,K.amb);R(1.85,-3.7,.13,1.4,.04,'#6B6F7E',.8)}
 if(ty!=6){x.strokeStyle='rgba(43,37,64,.45)';x.lineWidth=SW*.6;x.beginPath();x.moveTo(L*.46,-1.1);x.lineTo(L*.46,-.42);x.stroke();R(L*.5,-.95,.22,.05,.02,'rgba(255,255,255,.75)');R(-.05,-.58,.24,.22,.08,DK);R(L-.19,-.58,.24,.22,.08,DK);R(L-.06,-.4,.22,.07,.02,'#8A8FA3')}
 (ty==6?[1.0,L-1.7,L-.75]:[L*.2,L*.8]).forEach(wx=>wh(wx,r,sp));
 O(.12,ty==6?-1.1:-.85,.14,'#FFF3B0');const tly=ty==6?-1.3:-.95;R(L-.17,tly,.15,.25,.06,brake?K.red:'#8A2B35');if(brake)GL(L,tly+.1,.9,K.red,.7);
 if(hz){x.globalAlpha=Math.sin(hz)>0?1:.15;O(.08,-.6,.1,K.amb);O(L-.08,-.6,.1,K.amb);x.globalAlpha=1}
 x.restore();SW=3}
/* ===== MOTOR ===== */
const JK=['#F5A524','#2F86C9','#EF4444','#8E7CC3','#5BC0BE','#4A3B63','#F4F1EA'],HL=['#EF4444','#FFD23F','#2F86C9','#F4F1EA','#5BC0BE','#E86F9A','#2B2540'];
const NM=18,MCF=[];for(let i=0;i<NM;i++){const h=hh(i,21),ty=h<.36?0:h<.54?1:h<.72?2:h<.86?3:4,pk=a=>Math.floor(hh(i,a)*7);MCF.push({ty,body:CC[Math.floor(hh(i,23)*8)],jk:ty==2?'#2E9E5B':JK[pk(22)],jk2:JK[pk(24)],hel:ty==2?'#2E9E5B':HL[pk(25)],hel2:HL[pk(26)],full:hh(i,27)>.55,mask:hh(i,28)>.5,pass:hh(i,29)>.72,sk:SKN[Math.floor(hh(i,30)*4)]})}
const HK={ty:0,body:K.red,jk:'#FFD23F',hel:'#2F86C9',full:1,mask:0,sk:SKN[0]};
function rd(x0,jk,hel,full,mask,nod,sk){R(x0-.05,-.97,.78,.2,.1,'#3C3558');R(x0+.6,-.6,.26,.1,.04,INK);x.strokeStyle=jk;x.lineWidth=.11;x.lineCap='round';x.beginPath();x.moveTo(x0+.18,-1.38);x.lineTo(.33,-1.3);x.stroke();R(x0,-1.55,.5,.75,.2,jk,1);O(x0+.14,-1.72+nod,.17,sk,.8);
 if(full){R(x0-.06,-2.02+nod,.46,.36,.17,hel,.8);R(x0-.06,-1.84+nod,.22,.1,.04,DK)}else R(x0-.04,-1.99+nod,.42,.23,.11,hel,.8);if(mask)R(x0+.01,-1.7+nod,.18,.08,.03,'#E8F0F8')}
function moto(a,gy,m,cf,nod,brake,sp,pitch){x.save();x.translate(a,gy);x.scale(m,m);SW=sw0(m);E(.95,0,1.1,.18,'rgba(43,37,64,.3)');x.translate(.95,0);x.rotate(pitch);x.translate(-.95,0);
 const ty=cf.ty,mt=ty==0||ty==2||ty==3,r=mt?.27:.31,sk=cf.sk;
 [.38,1.52].forEach(wx=>{O(wx,-r,r,INK);O(wx,-r,r*.5,'#D7DCE4');x.strokeStyle=INK;x.lineWidth=SW*.7;for(let k=0;k<2;k++){const q=sp+k*1.57;x.beginPath();x.moveTo(wx+Math.cos(q)*r*.45,-r+Math.sin(q)*r*.45);x.lineTo(wx-Math.cos(q)*r*.45,-r-Math.sin(q)*r*.45);x.stroke()}});
 if(mt){R(.45,-.52,.95,.14,.06,DK);R(.5,-.92,1.1,.5,.25,cf.body,1);R(.18,-1.22,.3,.98,.13,cf.body,1);R(1.5,-.94,.42,.2,.08,cf.body,1);R(.75,-1.04,.72,.16,.07,DK)}
 else{R(.55,-1.1,.55,.3,.12,cf.body,1);R(.45,-.86,.85,.3,.1,'#6B6F7E',1);R(.95,-1.05,.6,.15,.06,DK);R(1.45,-1.02,.45,.07,.02,'#8A8FA3')}
 x.strokeStyle=DK;x.lineWidth=.07;x.lineCap='round';x.beginPath();x.moveTo(.38,-.4);x.lineTo(.3,-1.3);x.moveTo(.22,-1.33);x.lineTo(.5,-1.36);x.stroke();
 R(.04,-1.12,.22,.2,.09,'#FFF3B0',.8);R(1.8,-.9,.15,.12,.05,brake?K.red:'#8A2B35');R(1.4,-.46,.5,.08,.03,'#8A8FA3');if(brake)GL(1.9,-.84,.7,K.red,.6);
 if(ty==2){R(1.25,-1.62,.72,.7,.09,'#2E9E5B',1);R(1.25,-1.62,.72,.12,.05,'#237A46')}
 if(ty==4){R(1.2,-1.55,.85,.55,.05,'#C48A4A',1);R(1.3,-2.05,.65,.5,.05,'#E8B84A',1);x.strokeStyle=DK;x.lineWidth=.04;x.beginPath();x.moveTo(1.15,-1.8);x.lineTo(2.05,-1.8);x.stroke()}
 if(ty==3){R(1.1,-1.55,.5,.75,.2,cf.jk2,1);O(1.25,-1.72+nod,.17,sk,.8);R(1.19,-1.99+nod,.4,.23,.11,cf.hel2,.8);O(.5,-1.42,.1,sk,.6);R(.42,-1.32,.17,.34,.06,'#FFD23F',.8)}
 else if(cf.pass&&ty<2){R(1.12,-1.55,.5,.75,.2,cf.jk2,1);O(1.27,-1.72+nod,.17,sk,.8);R(1.21,-1.99+nod,.4,.23,.11,cf.hel2,.8)}
 rd(ty==3?.55:.72,cf.jk,cf.hel,cf.full,cf.mask,nod,sk);
 x.restore();SW=3}
/* ===== MANUSIA ===== */
const PL=[{t:'#2F86C9',b:'#3C3558',h:INK,bag:'back'},{t:'#F4F1EA',b:'#8A8FA3',h:INK,bag:'back',bc:'#EF4444'},{t:'#8E7CC3',b:'#3C3558',hj:'#F4D06F',bag:'hand',long:1},{t:'#E86F9A',b:'#2B2540',h:INK,bag:'tote',ph:1},{t:'#F5A524',b:'#2F6F9E',h:'#4A3B63',cap:'#EF4444',bag:'none'},{t:'#5BC0BE',b:'#6B6F7E',h:'#C9CED6',el:1,cane:1,bag:'none'},{t:'#F4F1EA',b:'#2B2540',h:INK,bag:'brief'},{t:'#4ADE80',b:'#3C3558',hj:'#EF4444',bag:'back',long:1,kid:1},{t:'#EF4444',b:'#3C3558',h:INK,bag:'hand',umb:'#2F86C9'},{t:'#FFD23F',b:'#2B2540',hj:'#2F86C9',bag:'tote',long:1,umb:'#E86F9A'}];
function body(P,ph,sk,fine){const s=Math.sin(ph),b=Math.abs(s)*.04;
 if(P.long){R(-.27,-.95,.54,.9,.1,P.b,1);R(-.2+s*.1,-.1,.28,.1,.04,INK);R(.02-s*.1,-.1,.28,.1,.04,INK)}
 else{x.strokeStyle=P.b;x.lineWidth=.15;x.lineCap='round';x.beginPath();x.moveTo(-.1,-.85);x.lineTo(-.1+s*.24,-.08);x.moveTo(.1,-.85);x.lineTo(.1-s*.24,-.08);x.stroke();R(-.2+s*.24,-.12,.3,.12,.05,INK);R(.02-s*.24,-.12,.3,.12,.05,INK)}
 if(P.bag=='back')R(-.42,-1.42-b,.22,.52,.08,P.bc||K.amb,1);
 R(-.27,-1.45-b,.54,.72,.2,P.t,1);
 const hx=P.ph?.3:-s*.2,hy=P.ph?-1.5:-.88;x.strokeStyle=P.t;x.lineWidth=.1;x.lineCap='round';x.beginPath();x.moveTo(0,-1.33-b);x.lineTo(hx,hy);x.stroke();O(hx,hy,.06,sk);
 if(P.bag=='hand')R(hx-.1,hy+.02,.32,.28,.07,K.amb,1);if(P.bag=='brief')R(hx-.1,hy+.02,.38,.26,.05,'#6B4A3A',1);if(P.bag=='tote'){R(hx-.08,hy+.02,.3,.36,.06,'#F4F1EA',1);x.strokeStyle='#C9CED6';x.lineWidth=.03;x.beginPath();x.moveTo(.1,-1.4);x.lineTo(hx,hy+.02);x.stroke()}
 if(P.ph){R(.27,-1.6,.1,.17,.02,DK);GL(.33,-1.52,.5,'#BDE8FF',.5)}
 if(P.cane){x.strokeStyle='#8B5A3C';x.lineWidth=.05;x.beginPath();x.moveTo(hx,hy);x.lineTo(hx+.05,0);x.stroke()}
 O(0,-1.62-b,.17,sk,.8);
 if(P.hj){R(-.2,-1.85-b,.4,.56,.2,P.hj,.8);O(.07,-1.62-b,.115,sk)}else if(P.h)R(-.19,-1.84-b,.38,.15,.07,P.h);
 if(P.cap){R(-.19,-1.84-b,.38,.11,.05,P.cap,.6);R(.1,-1.77-b,.17,.04,.02,P.cap)}
 if(fine){O(.09,-1.65-b,.024,INK);x.strokeStyle=INK;x.lineWidth=.02;x.beginPath();x.arc(.09,-1.58-b,.04,.2,2.9);x.stroke()}}
function ppl(px,gy,m,pi,ph,dir,fine){const P=PL[pi%PL.length],sk=SKN[pi%4];x.save();x.translate(px,gy);x.scale(dir*m,m);SW=sw0(m);E(0,0,.4,.1,'rgba(43,37,64,.25)');
 if(P.el)x.rotate(.07);body(P,ph,sk,fine);
 if(P.kid){x.save();x.translate(.62,0);x.scale(.55,.55);body({t:'#FFD23F',b:'#2F86C9',h:INK,bag:'none'},ph+1.3,sk,0);x.restore()}
 if(P.umb){x.strokeStyle=DK;x.lineWidth=.04;x.beginPath();x.moveTo(.05,-2.1);x.lineTo(.05,-1.4);x.stroke();x.beginPath();x.arc(.05,-2.1,.9,Math.PI,0);x.closePath();x.fillStyle=P.umb;x.fill();x.lineWidth=.05;x.stroke()}
 x.restore();SW=3}
/* ===== LATAR STATIS (digambar sekali) ===== */
let BGa,BGb;const mk=(w,h)=>{const c=document.createElement('canvas');c.width=w;c.height=h;return c};
function prep(cv,fn){x=cv.getContext('2d');x.translate(140,260);fn();x=MAIN}
function tw(a,gy,m,wm,hm,c,fl,cw,seed,bb){U(a,gy,m,()=>{R(0,-hm,wm,hm,.4,c,1);x.fillStyle='rgba(60,40,90,.14)';x.fillRect(wm*.7,-hm,wm*.3,hm);
 const rows=Math.floor(hm/fl),cols=Math.floor(wm/cw);for(let r=0;r<rows;r++){if(gy-(r+1)*fl*m<-140)break;for(let k=0;k<cols;k++){x.fillStyle=hh(a*.1+k,r+seed)>.45?'#FFEFB5':'rgba(70,80,120,.4)';x.fillRect(.5+k*cw,-(r+1)*fl+.5,cw*.55,fl*.5);if(m>9&&hh(a*.3+k,r+5)>.86)R(.4+k*cw,-(r+1)*fl+1.9,1.2,.5,.06,'#DDE2EA',.5)}}
 if(gy-hm*m>-100){if(hh(a,seed+9)>.45){R(wm*.3,-hm-1.3,wm*.22,1.3,.12,'#9AA3B5',.8);R(wm*.3,-hm-1.45,wm*.22,.25,.1,'#6B7080',.6)}x.strokeStyle='#6B7080';x.lineWidth=.12;x.beginPath();x.moveTo(wm*.8,-hm);x.lineTo(wm*.8,-hm-2.5);x.stroke()}
 if(bb){R(wm*.1,-hm-4.3,wm*.8,3,.2,'#2F86C9',1);R(wm*.1,-hm-4.3,wm*.8,.9,.2,'#EF4444',1);for(let k=0;k<4;k++)R(wm*.18+k*wm*.18,-hm-2.9,wm*.1,1.4,.05,'#FFE9A8')}})}
function build(){
 BGa=mk(1560,1000);prep(BGa,()=>{const g=x.createLinearGradient(0,0,0,470);[[0,'#2E7BD0'],[.45,'#7CC4F0'],[.78,'#FFD9A0'],[1,'#FFA55C']].forEach(a=>g.addColorStop(a[0],a[1]));x.fillStyle=g;x.fillRect(-140,-260,1560,1000);GL(930,372,340,'#FFE08A',.65);O(930,376,46,'#FFF4C2')});
 BGb=mk(1560,1000);prep(BGb,()=>{
  const TC=['#B9C6E2','#D5B9D6','#F3C9A0','#A8BEDB','#E8D2B8','#C6CCE6'],AC=['#F2A65A','#E87A90','#6DA9D2','#F4D06F','#A58FD1','#7FD1B9'],RB=['#FFF4E0','#FDE8C8','#F8DDD0','#E5EEF8','#F5F0D0'],RC=['#EF4444','#F5A524','#2F86C9','#E86F9A','#5BC0BE','#FFD23F'];
  for(let i=0;i<14;i++)tw(i*100-40,416,mp(416),17+hh(i,1)*4,45+hh(i,2)*65,TC[i%6],3.6,3,1,0);
  let g=x.createLinearGradient(0,150,0,470);g.addColorStop(0,'rgba(190,160,140,0)');g.addColorStop(1,'rgba(190,150,120,.5)');x.fillStyle=g;x.fillRect(-140,150,1560,330);
  for(let i=0;i<6;i++)tw(i*250-60,442,mp(442),17+hh(i,3)*5,16+hh(i,4)*18,AC[i%6],3.4,3.2,2,i==3);
  for(let i=0;i<12;i++){const hm=6.2+hh(i,5)*.6,c1=RC[i%6],c2=RC[(i+3)%6];U(i*107-20,470,21,()=>{R(0,-hm,5,hm,.15,RB[i%5],1);R(-.1,-hm-.25,5.2,.3,.1,'#B7A99A',1);R(.3,-3.95,4.4,.65,.12,c1,.8);x.fillStyle='rgba(255,255,255,.7)';for(let k=0;k<6;k++)x.fillRect(.55+k*.65,-3.8,.38,.2);R(.1,-3.2,4.8,.4,.1,c2,.8);R(.3,-2.75,4.4,2.45,.1,'#FFE9A8',.8);
   x.fillStyle='rgba(43,37,64,.55)';x.fillRect(.4,-2.65,.12,2.3);x.fillRect(4.4,-2.65,.12,2.3);for(let k=0;k<5;k++)O(.8+k*.85,-.7,.2,RC[(i+k)%6]);R(.5,-5.8,1.6,1.5,.12,'#9FC9E8',.8);R(2.9,-5.8,1.6,1.5,.12,'#9FC9E8',.8);R(2.7,-4.35,2,.18,0,'#8A8FA3',.6);if(hh(i,6)>.5){R(3.1,-5.2,.6,.5,.05,'#DDE2EA',.5)}})}
  [40,230,420,610,800,990,1180].forEach(px=>U(px,283,21,()=>{R(-.08,-7.2,.16,7.2,.03,'#5B6578',.6);R(-.08,-7.2,1.5,.14,.05,'#5B6578',.6);R(1.1,-7.12,.65,.2,.08,'#FFE9A8',.6)}));GL(40,140,60,'#FFE9A8',.3);
  U(1000,283,21,()=>{R(-.1,-6.8,.2,6.8,.03,'#5B6578',.7);R(-2.9,-7.3,3.8,2.2,.12,'#1E6FB8',1);x.strokeStyle='#fff';x.lineWidth=.14;x.lineCap='round';x.beginPath();x.moveTo(-2.3,-6.2);x.lineTo(-.9,-6.2);x.moveTo(-1.3,-6.7);x.lineTo(-.8,-6.2);x.lineTo(-1.3,-5.75);x.moveTo(-.3,-6.7);x.lineTo(.5,-6.7);x.moveTo(.1,-6.95);x.lineTo(.5,-6.7);x.lineTo(.1,-6.45);x.stroke()});
  [210,640,1070].forEach(p=>{R(p-15,321,30,149,3,'#A5A9BC',1.2);R(p-36,313,72,15,3,'#8A8FA3',1.2)});
  let sg=x.createLinearGradient(0,321,0,362);sg.addColorStop(0,'rgba(43,37,64,.38)');sg.addColorStop(1,'rgba(43,37,64,0)');x.fillStyle=sg;x.fillRect(-140,321,1560,42);
  R(-140,298,1560,23,0,'#8A8FA3',1.2);x.fillStyle='rgba(43,37,64,.22)';x.fillRect(-140,312,1560,9);x.fillStyle='rgba(255,255,255,.25)';x.fillRect(-140,299,1560,3);for(let k=-1;k<24;k++)x.fillRect(k*68,303,2,18);
  [330,545,905,1150].forEach(tx=>U(tx,474,21,()=>{R(-.15,-3.4,.3,3.4,.05,'#8B5A3C',.8);O(0,-5.2,2,'#4FA654');O(-1.5,-4.3,1.5,'#4FA654');O(1.5,-4.3,1.5,'#4FA654');O(.2,-5.6,1.5,'#63B968')}));
  [455,800].forEach(fx0=>U(fx0,474,21,()=>{R(-.05,-6.6,.1,6.6,.03,INK)}));
  U(725,476,21,()=>{R(-1.2,-1.1,2.4,.8,.1,K.amb,1);O(-.8,-.25,.3,INK);O(.8,-.25,.3,INK);R(-.4,-1.4,.8,.3,.1,'#C9CED6',.8);R(-.04,-3.3,.08,2.2,.02,INK);for(let k=0;k<6;k++){x.beginPath();x.moveTo(0,-3.3);x.arc(0,-3.3,1.8,Math.PI+k*Math.PI/6,Math.PI+(k+1)*Math.PI/6);x.closePath();x.fillStyle=k%2?'#FFF4E0':K.red;x.fill()}});
  U(1236,476,21,()=>{R(-.06,-5.2,.12,5.2,.03,'#5B6578',.8);R(-.4,-6.9,.8,1.7,.2,INK)});
  x.fillStyle='#CDBFA6';x.fillRect(-140,470,1560,14);x.fillStyle='#E8DCC4';x.fillRect(-140,483,1560,3);
  g=x.createLinearGradient(0,486,0,690);g.addColorStop(0,'#7A7F94');g.addColorStop(1,'#464B5C');x.fillStyle=g;x.fillRect(-140,486,1560,204);
  x.fillStyle='rgba(30,25,45,.18)';[[200,560,90,10],[760,590,120,12],[1100,548,70,7]].forEach(p=>{x.beginPath();x.ellipse(p[0],p[1],p[2],p[3],0,0,7);x.fill()});x.fillStyle='rgba(20,18,30,.3)';[[430,578,26,6],[950,620,34,8]].forEach(p=>{x.beginPath();x.ellipse(p[0],p[1],p[2],p[3],0,0,7);x.fill();x.strokeStyle='rgba(255,255,255,.18)';x.lineWidth=2;x.stroke()});
  x.fillStyle='#CDBFA6';x.fillRect(-140,512,1560,12);for(let k=-1;k<34;k++){O(k*46+8,512,7,'#4FA654');if(k%3==0)O(k*46+24,508,5,'#E86F9A')}
  x.fillStyle='rgba(255,255,255,.8)';for(let k=-1;k<5;k++){x.fillRect(k*389+30,584,167,8);x.fillRect(k*490+120,638,210,10)}
  x.save();x.translate(1180,654);x.scale(1,.42);TXT('BUS',0,0,72,'rgba(255,255,255,.6)');x.restore();
  x.fillStyle='#E8DCC4';x.fillRect(-140,690,1560,8);x.fillStyle='#D8CDB8';x.fillRect(-140,698,1560,60);x.fillStyle='#F4C531';x.fillRect(-140,700,1560,9);x.fillStyle='rgba(43,37,64,.28)';for(let k=-1;k<64;k++){x.fillRect(k*22+3,702,10,2);x.fillRect(k*22+3,706,10,2)}x.fillStyle='rgba(43,37,64,.12)';x.fillRect(-140,722,1560,3);
  const PX=[-420,95,600,1010,1420];PX.forEach(px=>{if(px>-60&&px<1340)U(px,482,24,()=>{R(-.12,-9,.24,9,.03,'#6B5A4A',.7);R(-1.4,-8.7,2.8,.16,0,'#6B5A4A',.5);[-1.1,0,1.1].forEach(o=>R(o-.07,-8.95,.14,.3,.04,'#C9CED6',.4))})});
  x.strokeStyle='#2B2540';x.lineWidth=1.3;for(let i=0;i<PX.length-1;i++)[272,281,290].forEach((yy,j)=>{x.beginPath();x.moveTo(PX[i]+(j-1)*26,yy);x.quadraticCurveTo((PX[i]+PX[i+1])/2,yy+38+j*2,PX[i+1]+(j-1)*26,yy);x.stroke()});
 })}
/* ===== LALU LINTAS: simulasi mengikuti kendaraan di depan (IDM); tiap kendaraan punya ritme sendiri ===== */
const T0=-3,DT=1/30,TS=Math.round((9.5-T0)/DT)+1;
const ON={y:532,dir:1,free:1,v0:9,g0:3,pool:[0,1,2,3,4,5,6],seed:15},LA={y:560,dir:-1,v0:4,g0:1.5,pool:[0,1,2,3,4,5],seed:5},LB={y:612,dir:-1,v0:3.6,g0:1.8,pool:[0,1,2,4,5,6,0,3],seed:9},FLY={y:283,m:21,dir:-1,v0:4.5,g0:1.3,pool:[0,1,2,3,4,6],mo:.3,seed:30},LN={ON,LA,LB};
function mkLane(o){o.m=o.m||mp(o.y);o.M=Math.max(...o.pool.map(k=>VT[k].L))*o.m+20;const veh=[],need=(1280+2*o.M)/o.m;let sum=0,i=0;
 while(sum<need||veh.length<4){if(o.mo&&hh(i,o.seed+5)<o.mo)veh.push({k:'m',len:1.9,mi:(i*3+5)%NM});else{const ty=o.pool[Math.floor(hh(i,o.seed)*o.pool.length)];veh.push({k:'c',ty,len:VT[ty].L,c:ty==3?'#FFD23F':CC[Math.floor(hh(i,o.seed+3)*8)]})}sum+=veh[i].len+o.g0;i++}
 const N=veh.length,Lm=sum,P=new Float32Array(TS*N),V=new Float32Array(TS*N),wv=veh.map((v,k)=>.9+hh(k,o.seed+1)*1.5),pv=veh.map((v,k)=>hh(k,o.seed+2)*6.28);
 let p=[],sp=[],c=0;veh.forEach((v,k)=>{c+=v.len;p[k]=c;c+=o.g0;sp[k]=o.v0*.3});
 for(let st=0;st<TS;st++){const t=T0+st*DT;for(let k=0;k<N;k++){P[st*N+k]=p[k];V[st*N+k]=sp[k]}
  const np=[],nv=[];for(let k=0;k<N;k++){const j=(k+1)%N,gap=Math.max(((p[j]-veh[j].len-p[k])%Lm+Lm)%Lm,.05),v0i=o.free?o.v0*(.88+.12*Math.sin(wv[k]*t+pv[k])):o.v0*cl(1.35*Math.sin(wv[k]*t+pv[k])+.1,0,1),v0e=Math.max(v0i,.25),dv=sp[k]-sp[j],ss=1+Math.max(0,sp[k]*1.1+sp[k]*dv/(2*Math.sqrt(3.2)));
   const a=cl(1.6*(1-Math.pow(sp[k]/v0e,4)-(ss/gap)*(ss/gap)),-7,1.6),v=Math.max(0,sp[k]+a*DT);nv[k]=v;np[k]=p[k]+v*DT}p=np;sp=nv}
 o.veh=veh;o.N=N;o.Lm=Lm;o.Lpx=Lm*o.m;o.P=P;o.V=V}
function sims(){[ON,LA,LB,FLY].forEach(o=>{if(!o.P)mkLane(o)})}
const tix=t=>{const s=cl((t-T0)/DT,0,TS-1.001),a=Math.floor(s);return[a,s-a]};
const lpos=(o,i,t)=>{const[a,f]=tix(t);return o.P[a*o.N+i]*(1-f)+o.P[(a+1)*o.N+i]*f};
const lvel=(o,i,t)=>{const[a,f]=tix(t);return o.V[a*o.N+i]*(1-f)+o.V[(a+1)*o.N+i]*f};
const lacc=(o,i,t)=>{const[a]=tix(t);return(o.V[(a+1)*o.N+i]-o.V[a*o.N+i])/DT};
const lx=(o,i,t)=>{const p=lpos(o,i,t)*o.m;return(o.dir<0?(((-p)%o.Lpx)+o.Lpx)%o.Lpx:((p%o.Lpx)+o.Lpx)%o.Lpx)-o.M};
const vlen=(o,i)=>o.veh[i].k=='c'?VT[o.veh[i].ty].L:1.9,la=(o,i,t)=>{const f=lx(o,i,t);return o.dir<0?f:f-vlen(o,i)*o.m};
function plume(pf,ex,ey,L,dir,gy,m,col,a0,t,seed,n){const p0=pf(t);for(let k=0;k<n;k++){const age=(t*.8+k/n+hh(seed,k))%1,pp=pf(t-age*1.3);if(Math.abs(pp-p0)>420)continue;const wx=pp+(dir<0?ex:(L-ex))*m+(age*.8+Math.sin(age*5+k+seed)*.12)*m,wy=gy+ey*m-age*1.3*m,r=(.14+age*.75)*m;if(LOW&&k%2)continue;O(wx,wy,r,rgba(col,a0*Math.pow(1-age,1.3)*Math.min(1,age*7)))}}
function lane(t,o,EN){for(let i=0;i<o.N;i++){const v=o.veh[i],T=v.k=='c'?VT[v.ty]:null,Lm=vlen(o,i),a=la(o,i,t);if(a>1400||a+Lm*o.m<-140)continue;
 const sp=lpos(o,i,t)/(T?T.r:.3)*(o.dir<0?1:-1),vv=lvel(o,i,t),ac=lacc(o,i,t),br=ac<-.5||vv<.25,pitch=cl(.006*ac,-.03,.03),vn=o.free?1:cl(vv/o.v0,0,1),hz=T&&v.ty==4&&vv<.25?t*9:0;
 const f=()=>{if(T){car(a,o.y,o.m,v.c,v.ty,br,o.dir,sp,o.free,pitch,hz);plume(tt=>la(o,i,tt),T.em[0],T.em[1],T.L,o.dir,o.y,o.m,VS[v.ty],VA[v.ty]*(.55+.45*(1-vn)),t,i+o.seed,4)}else{moto(a,o.y,o.m,MCF[v.mi],Math.sin(t*6+i)*.03,br,sp,pitch);plume(tt=>la(o,i,tt),1.9,-.4,1.9,-1,o.y,o.m,'#C4CCE0',.4,t,i+o.seed,2)}};
 if(EN)EN.push({g:o.y,f});else f()}}
function flyFront(){R(-140,277,1560,21,0,'#C3C6D4',1.2);R(-140,274,1560,5,0,'#E5E8F0',.8);x.fillStyle='rgba(43,37,64,.22)';for(let k=-1;k<28;k++)x.fillRect(k*52,280,2,18);x.fillStyle='rgba(255,255,255,.35)';x.fillRect(-140,281,1560,3)}
const mD=(i,t)=>212*(t+.3*Math.sin(1.3*t+i*1.9)),mpos=(i,t)=>(((i*127.5-mD(i,t))%2295)+2295)%2295-300,moy=(i,t)=>586+(hh(i,11)-.5)*10+12*Math.sin(1.7*t+i*1.9);
const HORNS=[{t:.32,L:'LB',x:880,s:'TIIIN!',k:'car'},{t:.62,L:'LA',x:330,s:'TEET!',k:'car2'},{t:1.0,L:'MO',x:560,s:'pip-pip!',k:'moto'},{t:1.45,L:'LB',x:260,s:'TOOOT!',k:'truck'},{t:1.9,L:'LA',x:900,s:'TIIN!',k:'car'},{t:2.15,L:'LB',x:700,s:'TEEET!',k:'angkot'},{t:2.5,L:'MO',x:220,s:'pip!',k:'moto'}];
function hornFx(h,t,EN){const q=(t-h.t)/.85;if(q<0||q>1)return;let bi=0,bd=1e9,px,gy,m,wd;
 if(h.L=='MO'){for(let i=0;i<NM;i++){const d=Math.abs(mpos(i,h.t)-h.x);if(d<bd){bd=d;bi=i}}px=mpos(bi,t);gy=moy(bi,t);m=mp(gy);wd=1.9*m}
 else{const o=LN[h.L];for(let i=0;i<o.N;i++){const d=Math.abs(la(o,i,h.t)-h.x);if(d<bd){bd=d;bi=i}}px=la(o,bi,t);gy=o.y;m=o.m;wd=vlen(o,bi)*m}
 EN.push({g:gy+.3,f:()=>{const cx=px+wd*.4,cy=gy-1.8*m;for(let k=0;k<3;k++){x.strokeStyle='rgba(255,255,255,'+((1-q)*.85*(1-k*.2))+')';x.lineWidth=Math.max(2,m*.07);x.beginPath();x.arc(cx,cy,(.6+q*2+k*.6)*m,-2.6,-.55);x.stroke()}
  x.save();x.translate(cx,cy-2.1*m-q*10);const z=(.7+eo(seg(q,0,.15))*.5)*cl(m/45,.55,1.1);x.scale(z,z);x.globalAlpha=1-sm(seg(q,.6,1));TXT(h.s,0,0,32,K.gld,1);x.restore()}})}
function bus(t,u){const bxAt=tt=>1400*(1-eo(seg(tt,2.6,4.2))),bx=bxAt(t),m=mp(665),mov=bx>2,d=t-4.2,sw=d>0?Math.sin(d*9)*Math.exp(-d*2.5)*.06:0,brk=t>3.3&&t<4.4,ang=bx/(m*.5),p=eo(seg(t,4.2,5.0)),ua=sm(seg(u,.35,1)),fa=1-sm(seg(u,.5,1)),BL='#2F7FC1',BD='#1F5F9E',SH=['#2F6F9E','#8E7CC3','#C0504D','#3C3558','#4A7C59','#E86F9A'],SK=['#8D5A3B','#B07A58','#D9A07A'];
 if(t<5.4)for(let k=0;k<7;k++){const age=(t*1.1+k/7)%1,tp=t-age*1.2;if(tp<2.5)continue;const wx=640-6*m+bxAt(tp)+11.9*m+(age*.9+Math.sin(age*5+k)*.1)*m,wy=665-.6*m-age*1.6*m;O(wx,wy,(.12+age*.6)*m,rgba('#34323F',(tp<4.4?.55:.28)*Math.pow(1-age,1.3)*Math.min(1,age*7)))}
 x.save();x.translate(640-6*m+bx,665+(mov?Math.sin(t*14)*1.2:0)+sw*m);x.scale(m,m);SW=sw0(m);
 E(6,.05,6.3,.28,'rgba(43,37,64,.3)');if(mov)beam(0,-.9,5,.4);
 /* badan, lapisan warna dan bayangan */
 R(0,-3.25,12,2.7,.45,BL,1.2);x.save();x.beginPath();x.roundRect(0,-3.25,12,2.7,.45);x.clip();
 let g=x.createLinearGradient(0,-3.25,0,-.55);g.addColorStop(0,'rgba(255,255,255,.22)');g.addColorStop(.35,'rgba(255,255,255,0)');g.addColorStop(1,'rgba(20,30,60,.25)');x.fillStyle=g;x.fillRect(0,-3.25,12,2.7);
 x.fillStyle='#F4F7FB';x.fillRect(0,-3.25,12,.2);x.fillStyle='#2A3F63';x.fillRect(0,-.84,12,.3);x.fillStyle=K.apl;x.fillRect(0,-1.2,12,.2);x.fillStyle=K.amb;x.fillRect(0,-1.0,12,.12);
 x.fillStyle='rgba(20,30,60,.35)';[1.1,4.95,7.05,11.3].forEach(a=>x.fillRect(a,-3.0,.03,2.2));for(let k=0;k<5;k++)O(1.4+k*2.3,-1.1,.04,K.amb);x.restore();R(0,-3.25,12,2.7,.45,0,1.2);
 /* atap: AC, kisi-kisi, antena */
 R(3.9,-3.58,2.6,.36,.12,'#D7DEE8',.9);x.strokeStyle='rgba(43,37,64,.35)';x.lineWidth=.03;for(let k=0;k<7;k++){x.beginPath();x.moveTo(4.1+k*.33,-3.52);x.lineTo(4.1+k*.33,-3.3);x.stroke()}
 R(8.4,-3.44,.9,.2,.07,'#D7DEE8',.8);x.strokeStyle=INK;x.lineWidth=.05;x.beginPath();x.moveTo(11.2,-3.25);x.lineTo(11.4,-4);x.stroke();O(11.4,-4,.06,K.red);
 /* papan tujuan LED yang berjalan */
 R(4.45,-3.12,3.1,.44,.1,INK,.8);x.save();x.beginPath();x.roundRect(4.5,-3.1,3,.4,.08);x.clip();x.scale(1/m,1/m);x.font='800 '+(.26*m).toFixed(1)+'px Trebuchet MS,sans-serif';x.textAlign='left';const lb=BUSLABEL+'   ·   ',tw=Math.max(40,x.measureText(lb).width),off=-((t*38)%tw);x.fillStyle=K.amb;for(let k=0;k<3;k++)x.fillText(lb,4.5*m+off+k*tw+6,-2.82*m);x.restore();
 /* jendela penumpang */
 [[.8,1.55],[2.45,1.5],[4.05,.95],[7.05,1.45],[8.6,1.45],[10.15,1.1]].forEach((q,k)=>{const a=q[0],w=q[1];x.save();x.beginPath();x.roundRect(a,-2.78,w,1,.14);x.clip();
  const wg=x.createLinearGradient(0,-2.78,0,-1.78);wg.addColorStop(0,'#FFF3C4');wg.addColorStop(1,'#FFD98A');x.fillStyle=wg;x.fillRect(a,-2.78,w,1);
  x.strokeStyle='#E6B800';x.lineWidth=.06;x.beginPath();x.moveTo(a,-2.52);x.lineTo(a+w,-2.52);x.stroke();
  const n=w>1.2?2:1;for(let j=0;j<n;j++){const px=a+(n==1?w/2:w*(.28+.44*j)),tp=Math.floor(hh(k*3+j,77)*5),bo=Math.sin(t*3+k+j)*.025,sh=SH[Math.floor(hh(k,j+9)*6)],sk=SK[Math.floor(hh(k+4,j)*3)];
   if(tp==0||tp==2){R(px-.24,-1.84+bo,.48,.9,.2,sh);O(px,-2.02+bo,.16,sk);if(tp==2){R(px-.21,-2.2+bo,.42,.42,.2,'#F4D06F');O(px+.04,-2.02+bo,.11,sk)}}
   else if(tp==1){R(px-.24,-2.24+bo,.48,1.2,.2,sh);O(px,-2.42+bo,.16,sk);x.strokeStyle=sh;x.lineWidth=.1;x.lineCap='round';x.beginPath();x.moveTo(px+.12,-2.1+bo);x.lineTo(px+.3,-2.5+bo);x.stroke()}
   else if(tp==3){R(px-.18,-1.78+bo,.36,.8,.16,sh);O(px,-1.93+bo,.12,sk)}else R(px-.2,-1.98,.4,.25,.1,'#B5453F')}
  const sx=Math.sin(t*3+k)*.06;x.strokeStyle='#DDE2EA';x.lineWidth=.03;x.beginPath();x.moveTo(a+w*.5,-2.52);x.lineTo(a+w*.5+sx,-2.25);x.stroke();O(a+w*.5+sx,-2.2,.06,'#EEF1F6');
  const gl=x.createLinearGradient(0,-2.78,0,-2);gl.addColorStop(0,'rgba(255,150,80,.3)');gl.addColorStop(1,'rgba(255,150,80,0)');x.fillStyle=gl;x.fillRect(a,-2.78,w,.8);
  x.fillStyle='rgba(255,255,255,.28)';x.beginPath();x.moveTo(a+w*.12,-2.78);x.lineTo(a+w*.36,-2.78);x.lineTo(a+w*.06,-1.78);x.lineTo(a-.18,-1.78);x.fill();x.restore();
  R(a,-2.78,w,1,.14,0,1);R(a-.04,-1.78,w+.08,.07,.03,BD,.6)});
 /* kabin pengemudi, lampu depan, bumper, kaca spion */
 R(.12,-2.78,.58,1,.14,'#9FD3EE',1);x.save();x.beginPath();x.roundRect(.12,-2.78,.58,1,.14);x.clip();O(.44,-2.1,.17,'#2A3F63');R(.3,-1.95,.36,.6,.14,'#2A3F63');x.strokeStyle=DK;x.lineWidth=.05;x.beginPath();x.ellipse(.2,-1.9,.05,.17,0,0,7);x.stroke();x.fillStyle='rgba(255,255,255,.3)';x.fillRect(.12,-2.78,.14,1);x.restore();
 R(-.1,-1.0,.4,.38,.1,'#2A3F63',1);R(0,-1.5,.24,.3,.08,'#FFF3B0',.8);if(mov)GL(.05,-1.35,.9,'#FFF3B0',.5);R(0,-1.15,.22,.1,.04,(mov||p>0)&&Math.sin(t*10)>0?K.amb:'#7A5A20',.6);
 x.strokeStyle=DK;x.lineWidth=.07;x.beginPath();x.moveTo(.1,-2.5);x.lineTo(-.22,-2.55);x.stroke();R(-.34,-2.82,.2,.5,.07,DK,.9);R(-.31,-2.78,.05,.4,.02,'#9FD3EE');
 /* belakang: lampu rem, kisi mesin, knalpot */
 R(11.8,-2.45,.18,.95,.06,brk?K.red:'#8A2B35',.8);if(brk)GL(11.9,-2,1.1,K.red,.6);R(10.55,-2.45,1.1,.8,.08,'#2A3F63',.8);x.strokeStyle='rgba(255,255,255,.25)';x.lineWidth=.03;for(let k=0;k<6;k++){x.beginPath();x.moveTo(10.65,-2.35+k*.11);x.lineTo(11.55,-2.35+k*.11);x.stroke()}
 R(11.65,-1.0,.35,.42,.1,'#2A3F63',1);R(11.55,-.68,.5,.1,.03,'#6B6F7E',.6);
 /* stiker: lencana rute, teks, simbol kursi roda */
 O(2.0,-1.46,.26,K.amb,.9);x.save();x.scale(1/m,1/m);TXT('05',2.0*m,-1.38*m,Math.round(.3*m),INK);TXT(DECAL,9.95*m,-1.36*m,Math.round(.23*m),'#F4F7FB');x.restore();
 R(7.25,-1.68,.42,.42,.08,'#2F6FD0',.8);x.strokeStyle='#fff';x.lineWidth=.035;x.lineCap='round';O(7.46,-1.58,.04,'#fff');x.beginPath();x.moveTo(7.46,-1.52);x.lineTo(7.46,-1.42);x.lineTo(7.57,-1.42);x.stroke();x.beginPath();x.arc(7.46,-1.4,.09,3.6,5.8);x.stroke();
 /* pintu lipat */
 R(5.25,-2.7,1.5,2.5,.14,INK);R(5.25,-2.84,1.5,.16,.05,'#F4F7FB',.8);R(5.38,-2.82,.13,.12,.03,'#2F6FD0');R(5.85,-2.83,.3,.1,.04,p>.02&&Math.sin(t*12)>0?K.amb:'#7A5A20',.6);
 x.save();x.beginPath();x.rect(5.4,-2.55,1.2,2.25);x.clip();const ig=x.createLinearGradient(0,-2.55,0,-.3);ig.addColorStop(0,'#2F415C');ig.addColorStop(1,'#1F2D44');x.fillStyle=ig;x.fillRect(5.4,-2.55,1.2,2.25);
 GL(6,-1.5,1.4,'#FFE9A8',.5*(1-ua));x.globalAlpha=fa;
 R(5.4,-2.5,1.2,.1,0,'#FFF3B0');R(5.5,-2.55,.08,2.25,.03,'#FFD23F',.7);R(6.42,-2.55,.07,2.25,.03,'#FFD23F',.7);R(5.4,-2.3,1.2,.06,0,'#FFD23F');R(5.62,-2.05,.55,.36,.04,'#F4F7FB',.5);R(5.62,-1.84,.55,.15,0,K.red);
 R(6.15,-1.45,.45,.75,.12,K.amb,1);O(6.38,-1.7,.14,'#B07A58');R(6.2,-1.58,.34,.64,.16,'#8E7CC3');
 [0,1].forEach(j=>{const sx=Math.sin(t*3+j)*.07;x.strokeStyle='#C9D3E0';x.lineWidth=.04;x.beginPath();x.moveTo(5.9+j*.35,-2.45);x.lineTo(5.9+j*.35+sx,-2.05);x.stroke();O(5.9+j*.35+sx,-1.98,.1,K.amb,.8)});
 R(5.4,-.75,1.2,.2,0,'#44556C');R(5.4,-.75,1.2,.05,0,'#FFD23F');R(5.4,-.48,1.2,.18,0,'#364760');R(5.4,-.48,1.2,.05,0,'#FFD23F');
 x.globalAlpha=ua;x.fillStyle=K.hb;x.fillRect(5.4,-2.55,1.2,2.25);x.globalAlpha=1;x.restore();
 const w=.6*(1-p);R(5.4,-2.55,w,2.25,.05,BL,1);R(6.6-w,-2.55,w,2.25,.05,BL,1);if(w>.2){x.globalAlpha=.9;R(5.45,-2.4,w-.1,1.2,.08,'#9FD3EE');R(6.55-w+.05,-2.4,w-.1,1.2,.08,'#9FD3EE');x.globalAlpha=1;R(5.4+w-.06,-2.55,.06,2.25,0,DK);R(6.6-w,-2.55,.06,2.25,0,DK)}
 R(5.25,-.3,1.5,.12,.03,'#44556C',.7);R(5.3,-.3,1.4,.04,0,'#FFD23F');
 /* roda: busur, ban bertapak, pelek 6 jari, baut, tutup lumpur */
 [2.2,9.6].forEach(wx=>{x.fillStyle=INK;x.beginPath();x.arc(wx,-.5,.64,Math.PI,0);x.fill();x.strokeStyle='#1B2A4A';x.lineWidth=.05;x.beginPath();x.arc(wx,-.5,.7,Math.PI,0);x.stroke();O(wx,-.5,.5,'#1E1B2C');
  x.strokeStyle='#3A3550';x.lineWidth=.04;for(let k=0;k<20;k++){const a=ang+k*Math.PI/10;x.beginPath();x.moveTo(wx+Math.cos(a)*.44,-.5+Math.sin(a)*.44);x.lineTo(wx+Math.cos(a)*.5,-.5+Math.sin(a)*.5);x.stroke()}
  O(wx,-.5,.3,'#C9D3E0',.8);x.strokeStyle='#8A93A8';x.lineWidth=.05;for(let k=0;k<6;k++){const a=ang+k*Math.PI/3;x.beginPath();x.moveTo(wx+Math.cos(a)*.07,-.5+Math.sin(a)*.07);x.lineTo(wx+Math.cos(a)*.27,-.5+Math.sin(a)*.27);x.stroke();O(wx+Math.cos(a+.52)*.16,-.5+Math.sin(a+.52)*.16,.025,DK)}O(wx,-.5,.07,DK);R(wx+.7,-.95,.16,.55,.03,DK,.6)});
 if(p>0){const sg=x.createLinearGradient(0,0,0,1.6);sg.addColorStop(0,rgba('#FFE9A8',.5*p*(1-u)));sg.addColorStop(1,rgba('#FFE9A8',0));x.fillStyle=sg;x.beginPath();x.moveTo(5.3,.02);x.lineTo(6.7,.02);x.lineTo(8,1.6);x.lineTo(4,1.6);x.fill()}
 x.restore();SW=3}
const WL=[[110,30,0],[140,30,7],[420,-26,2],[610,34,6],[960,-30,1],[990,-30,9],[1120,24,4],[250,-20,5],[820,28,8],[40,-34,3],[1300,-24,0],[520,22,9],[200,-18,2],[500,32,4],[700,-28,7],[880,18,3],[1050,-22,8],[330,26,5]];
function world(t,u){
 x.drawImage(BGa,-140,-260);
 [[200,110,1],[760,70,.8],[1100,150,.9],[470,175,.7]].forEach((c,i)=>{const q=((c[0]+t*(6+i*2))+200)%1700-220;x.globalAlpha=.92;[[0,0,70,20],[42,-12,40,18],[-40,-6,36,14]].forEach(e=>E(q+e[0]*c[2],c[1]+e[1]*c[2],e[2]*c[2],e[3]*c[2],i%2?'#FFE3D0':'#FFFFFF'));x.globalAlpha=1});
 x.strokeStyle='#4A3B63';x.lineWidth=2.5;x.lineCap='round';for(let i=0;i<6;i++){const bx=((t*42+i*260)%1500)-110,by=70+i*24+Math.sin(t*1.5+i)*8,fl=Math.sin(t*11+i)*5;x.beginPath();x.moveTo(bx-11,by-fl);x.quadraticCurveTo(bx-4,by-6,bx,by);x.quadraticCurveTo(bx+4,by-6,bx+11,by-fl);x.stroke()}
 x.drawImage(BGb,-140,-260);
 if(!LOW)for(let k=0;k<6;k++){const q=((k*340+t*14)%1800)-340;E(q,350+k*16,270,40,'rgba(150,125,110,.10)')}
 lane(t,FLY,null);flyFront();
 [455,800].forEach((fx0,j)=>U(fx0,474,21,()=>{for(let k=0;k<9;k++){const off=Math.sin(t*4-k*.5+j)*.28*(k/8);R(off,-6.6+k*.3,.7,.3,0,k%2?'#FFFFFF':K.red)}}));
 U(725,476,21,()=>{for(let k=0;k<3;k++){const q=(t*.6+k/3)%1;x.globalAlpha=.5*(1-q);O(-.5+Math.sin(q*6+k)*.2,-1.5-q*1.6,.15+q*.3,'#fff');x.globalAlpha=1}});
 const ph=t%6;U(1236,476,21,()=>{[[K.red,ph<2.6],['#F5A524',ph>=5],['#4ADE80',ph>=2.6&&ph<5]].forEach((l,i)=>{O(0,-6.5+i*.5,.17,l[1]?l[0]:'#4A4660');if(l[1])GL(0,-6.5+i*.5,1.2,l[0],.5)})});
 WL.forEach((w,i)=>ppl(((w[0]+t*w[1])%1500+1500)%1500-110,481,mp(481),w[2],t*5.5+i,w[1]>0?1:-1,0));
 ppl(690,481,mp(481),3,Math.sin(t*.8)*.1,1,0);ppl(765,479,mp(479),6,Math.sin(t*3)*.4,-1,0);ppl(662,481,mp(481),5,Math.sin(t*.7)*.1,1,0);
 const EN=[];lane(t,ON,EN);lane(t,LA,EN);lane(t,LB,EN);
 for(let i=0;i<NM;i++){const y=moy(i,t),m=mp(y),px=mpos(i,t),D=mD(i,t),acc=-212*.39*1.3*Math.sin(1.3*t+i*1.9),pt=.004*acc/m;
  EN.push({g:y,f:()=>{moto(px,y,m,MCF[i],Math.sin(t*6+i)*.03,Math.cos(1.3*t+i*1.9)>.75,D/(m*.3),pt);plume(tt=>mpos(i,tt),1.9,-.4,1.9,-1,y,m,'#C4CCE0',.4,t,i+40,2)}})}
 HORNS.forEach(h=>hornFx(h,t,EN));
 if(t>.1&&t<.95){const mx=1500-2333*(t-.15),gy=688,m=mp(gy);EN.push({g:gy,f:()=>{x.strokeStyle='rgba(255,255,255,.6)';x.lineWidth=4;x.lineCap='round';[[-60,-40],[-110,-70],[-30,-100]].forEach(l=>{x.beginPath();x.moveTo(mx+170-l[0],gy+l[1]);x.lineTo(mx+420-l[0],gy+l[1]);x.stroke()});moto(mx,gy,m,HK,Math.sin(t*30)*.03,false,mx/(m*.3),-.03)}})}
 if(t>2.5)EN.push({g:665,f:()=>bus(t,u)});
 EN.sort((a,b)=>a.g-b.g).forEach(e=>e.f());
}
function fg(t,u){
 x.save();x.translate(u*700,0);ppl(1195,722,mp(722),3,Math.sin(t*1.3)*.25,-1,1);x.restore();
 x.save();x.translate(-u*1000-22*sm(seg(t,1.4,2.6))*1.6,0);
 if(t<3.2)ppl(430-175*t,722,mp(722),1,t*5.2,-1,1);
 R(-40,-24,620,76,16,'#E9EEF5',4);R(-40,44,620,14,0,'#2F6F9E');R(26,52,26,700,8,'#5B6578',3);R(2,76,100,54,10,'#2F6F9E',3);TXT('ST-01',52,112,24,'#fff');
 R(190,56,3,26,0,'#5B6578');R(310,56,3,26,0,'#5B6578');R(160,82,180,46,9,INK,3);TXT('BUS 07 · 1 MNT',250,112,16,K.amb);if(Math.sin(t*6)>0)O(329,95,4,K.red);
 x.restore();
}
function fx(t,u){
 for(let i=0;i<18;i++){const ex=hh(i,5)*1280+Math.sin(t+i)*20,ey=720-((t*(24+hh(i,6)*30)+hh(i,7)*720)%720);x.globalAlpha=(.25+.35*Math.sin(t*3+i))*(1-u);O(ex,ey,1.5+hh(i,8)*2,'#FFE08A')}x.globalAlpha=1;
 const e=eio(u);if(e>0&&e<1){x.strokeStyle='#fff';x.lineWidth=2;x.globalAlpha=.4*Math.sin(e*Math.PI);for(let i=0;i<22;i++){const a=i*Math.PI*2/22+hh(i,9),r1=200+hh(i,3)*100,r2=r1+160;x.beginPath();x.moveTo(640+Math.cos(a)*r1,420+Math.sin(a)*r1*.7);x.lineTo(640+Math.cos(a)*r2,420+Math.sin(a)*r2*.7);x.stroke()}x.globalAlpha=1}
 x.fillStyle='rgba(125,105,95,.07)';x.fillRect(0,0,1280,720);
 const v=x.createRadialGradient(640,380,330,640,380,860);v.addColorStop(0,rgba('#3A1F3F',0));v.addColorStop(1,rgba('#3A1F3F',.4));x.fillStyle=v;x.fillRect(0,0,1280,720);
}
function draw(t){
 if(!BGa)build();if(!ON.P)sims();x.setTransform(1,0,0,1,0,0);x.fillStyle=K.hb;x.fillRect(0,0,1280,720);
 const u=seg(t,5.1,6.4),e=eio(u),hook=1-eo(seg(t,0,.9)),s=(1+.34*hook)*(1+14*e*e);
 x.save();x.translate(640,550);x.rotate(-.03*hook);x.scale(s,s);x.translate(-640,-550-Math.sin(u*Math.PI*2)*10);
 x.translate(-22*sm(seg(t,1.4,2.6))+Math.sin(t*1.1)*2,Math.sin(t*1.7)*1.5);world(t,u);x.restore();
 if(u<1)fg(t,u);fx(t,u);
 const f=seg(t,6.1,6.5);if(f>0){x.globalAlpha=f;x.fillStyle=K.hb;x.fillRect(0,0,1280,720);x.globalAlpha=1}
}

/* ===================== DOM, suara, dan alur (khusus modul) ===================== */
const DEF={greeting:'Hai, aku Mirza!',tag:'PORTOFOLIO · PWK ITS',description:'Sebelum masuk, ada animasi pembuka singkat (±8 detik) berisi gerakan kendaraan dan suara klakson. Pilih cara Anda menikmatinya; kapan saja bisa dilewati.',btnSound:'Mulai perjalanan · dengan suara',btnMute:'Tanpa suara',skipText:'Lewati ke portofolio',loading:'Menyiapkan kota…',ready:'Siap. Halte menunggu Anda.',soundOn:'Aktifkan suara',soundOff:'Matikan suara',skipBtn:'Lewati intro',busLabel:'ST-05 · PORTOFOLIO',busDecal:'URBAN TRANSIT · PWK ITS',once:false,storageKey:'halteIntroSeen',lockScroll:true,gate:true,heroBg:null,onStart:null,onDone:null};
let O=Object.assign({},DEF),root=null,gateEl=null,ctlEl=null,sndBtn=null,gbEl=null,gsEl=null,raf=0,t0=0,fired=[],fa=0,fn=0,AC=null,MG=null,snd=false,keyH=null,active=false,playing=false;
const H=document.documentElement;
const reduce=()=>!!(window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches);
const seenKey=()=>{try{return sessionStorage.getItem(O.storageKey)==='1'}catch(e){return false}};
const el=(tag,cls,txt)=>{const e=document.createElement(tag);if(cls)e.className=cls;if(txt!=null)e.textContent=txt;return e};
const cssHex=(n,fb)=>{const v=getComputedStyle(H).getPropertyValue(n).trim();return /^#[0-9a-f]{6}$/i.test(v)?v:fb};
const emit=n=>{try{window.dispatchEvent(new CustomEvent(n))}catch(e){}};
/* suara */
const ac=()=>AC||(AC=new(window.AudioContext||window.webkitAudioContext)());
const MGn=()=>{const a=ac();if(!MG){MG=a.createGain();MG.gain.value=0;MG.connect(a.destination)}return MG};
function fadeIn(){const a=ac(),g=MGn().gain;g.cancelScheduledValues(a.currentTime);g.setValueAtTime(0,a.currentTime);g.linearRampToValueAtTime(1,a.currentTime+.9)}
function tone(f,d,ty='square',v=.07){if(!snd)return;const a=ac(),o=a.createOscillator(),g=a.createGain();o.type=ty;o.frequency.value=f;g.gain.setValueAtTime(v,a.currentTime);g.gain.exponentialRampToValueAtTime(.001,a.currentTime+d);o.connect(g).connect(MGn());o.start();o.stop(a.currentTime+d)}
function noise(d,v,fq,ty='lowpass'){if(!snd)return;const a=ac(),n=Math.floor(a.sampleRate*d),b=a.createBuffer(1,n,a.sampleRate),h=b.getChannelData(0);for(let i=0;i<n;i++)h[i]=Math.random()*2-1;const s=a.createBufferSource();s.buffer=b;const f=a.createBiquadFilter();f.type=ty;f.frequency.value=fq;const g=a.createGain();g.gain.setValueAtTime(v,a.currentTime);g.gain.linearRampToValueAtTime(0,a.currentTime+d);s.connect(f).connect(g).connect(MGn());s.start()}
function horn(k){if(k=='car'){tone(420,.3,'square',.045);tone(528,.3,'square',.04)}else if(k=='car2'){[0,260].forEach(d=>setTimeout(()=>{tone(380,.18,'square',.045);tone(480,.18,'square',.04)},d))}else if(k=='moto'){[0,150].forEach(d=>setTimeout(()=>tone(900,.09,'square',.04),d))}else if(k=='truck'){tone(170,.8,'sawtooth',.06);tone(214,.8,'sawtooth',.05)}else{tone(310,.55,'square',.05);tone(390,.55,'square',.04)}}
const EV=[[0,()=>{noise(5.2,.05,500);tone(70,5,'sawtooth',.02)}],[.15,()=>{noise(.7,.14,1200,'bandpass');tone(110,.5,'sawtooth',.06)}],...HORNS.map(h=>[h.t,()=>horn(h.k)]),[1.2,()=>noise(.12,.08,900)],[2.7,()=>noise(1.5,.08,300)],[3.9,()=>noise(.5,.05,3000,'highpass')],[4.25,()=>noise(.45,.12,5000,'highpass')],[4.8,()=>tone(180,.08)],[5.35,()=>tone(140,.07)],[5.7,()=>tone(150,.07)],[6.3,()=>noise(.8,.07,1500,'bandpass')],[6.9,()=>{tone(660,.7,'sine',.1);tone(990,.7,'sine',.05)}]];
/* alur */
function finish(){if(!root&&!active)return;active=false;playing=false;cancelAnimationFrame(raf);
 if(keyH){document.removeEventListener('keydown',keyH);keyH=null}
 if(AC&&MG){try{const g=MG.gain;g.cancelScheduledValues(AC.currentTime);g.setValueAtTime(g.value,AC.currentTime);g.linearRampToValueAtTime(0,AC.currentTime+.25)}catch(e){}}
 if(O.once){try{sessionStorage.setItem(O.storageKey,'1')}catch(e){}}
 const r=root;root=null;if(r){r.classList.add('hi-out');setTimeout(()=>{if(r.parentNode)r.parentNode.removeChild(r)},650)}
 H.classList.remove('hi-pending','hi-lock');H.classList.add('hi-done');emit('halte-intro:done');if(O.onDone){try{O.onDone()}catch(e){}}}
function loop(){const t=(performance.now()-t0)/1000,c0=performance.now();draw(Math.min(t,8));fa+=performance.now()-c0;if(++fn==20){LOW=fa/20>22;fa=0;fn=0}
 EV.forEach((e,i)=>{if(!fired[i]&&t>=e[0]){fired[i]=1;e[1]()}});
 C.style.opacity=Math.min(seg(t,0,.5),1-seg(t,6.7,7.3));if(t>=7.4){finish();return}raf=requestAnimationFrame(loop)}
function start(){fired=[];playing=true;t0=performance.now();C.style.opacity=0;ctlEl.style.display='';if(O.onStart){try{O.onStart()}catch(e){}}emit('halte-intro:start');loop()}
function prepare(){return new Promise(res=>{const gr=[...root.querySelectorAll('.hi-rail i,.hi-rail b')];let k=0;const adv=n=>{while(k<n&&k<gr.length)gr[k++].classList.add('hi-on')},t1=performance.now();
 setTimeout(()=>{adv(3);build();adv(5);setTimeout(()=>{sims();adv(8);setTimeout(()=>{adv(9);setTimeout(res,Math.max(0,1100-(performance.now()-t1)))},30)},30)},60)})}
function setSound(on){snd=on;if(sndBtn)sndBtn.textContent=on?O.soundOff:O.soundOn;if(on){ac().resume();fadeIn()}}
function enter(sound){setSound(sound);gateEl.classList.add('hi-gone');start();setTimeout(()=>{if(gateEl)gateEl.style.display='none'},700)}
function mount(){
 K.hb=O.heroBg||cssHex('--color-hero-bg','#14211C');BUSLABEL=O.busLabel;DECAL=O.busDecal;
 root=el('div','hi-root');root.setAttribute('role','dialog');root.setAttribute('aria-modal','true');root.setAttribute('aria-label','Animasi pembuka portofolio');root.style.background=K.hb;root.style.setProperty('--hi-bg',K.hb);
 const stage=el('div','hi-stage');C.className='hi-canvas';C.setAttribute('aria-hidden','true');C.style.opacity=0;stage.appendChild(C);root.appendChild(stage);
 gateEl=el('div','hi-gate');const gw=el('div','hi-gw'),tg=el('p','hi-tag');tg.appendChild(el('i'));tg.appendChild(document.createTextNode(O.tag));
 const rail=el('div','hi-rail');for(let i=0;i<5;i++){rail.appendChild(el('i'));if(i<4)rail.appendChild(el('b'))}
 gsEl=el('p','hi-gs',O.loading);gsEl.setAttribute('aria-live','polite');gbEl=el('div','hi-gb');
 const b1=el('button','hi-btn',O.btnSound),b0=el('button','hi-b2',O.btnMute);b1.type=b0.type='button';gbEl.appendChild(b1);gbEl.appendChild(b0);
 const sk=el('a','hi-gl',O.skipText);sk.href='#';
 [tg,el('p','hi-hi',O.greeting),el('p','hi-gd',O.description),rail,gsEl,gbEl,sk].forEach(n=>gw.appendChild(n));gateEl.appendChild(gw);root.appendChild(gateEl);
 ctlEl=el('div','hi-ctl');sndBtn=el('button','hi-b',O.soundOn);const skb=el('button','hi-b',O.skipBtn);sndBtn.type=skb.type='button';ctlEl.appendChild(sndBtn);ctlEl.appendChild(skb);ctlEl.style.display='none';root.appendChild(ctlEl);
 document.body.appendChild(root);
 b1.onclick=()=>enter(true);b0.onclick=()=>enter(false);sk.onclick=e=>{e.preventDefault();finish()};skb.onclick=finish;sndBtn.onclick=()=>setSound(!snd);
 keyH=e=>{if(e.key==='Escape')finish()};document.addEventListener('keydown',keyH);
 if(O.gate){prepare().then(()=>{if(!root)return;gsEl.textContent=O.ready;gbEl.classList.add('hi-on');b1.focus()})}
 else{gateEl.style.display='none';build();sims();start()}}
function init(opts){if(active)return;O=Object.assign({},DEF,opts||{});
 if(reduce()||(!O.force&&O.once&&seenKey())){H.classList.remove('hi-pending');H.classList.add('hi-done');emit('halte-intro:done');if(O.onDone){try{O.onDone()}catch(e){}}return}
 active=true;H.classList.add('hi-pending');if(O.lockScroll)H.classList.add('hi-lock');
 if(document.body)mount();else document.addEventListener('DOMContentLoaded',mount,{once:true})}
function replay(){if(active)return;H.classList.remove('hi-done');init(Object.assign({},O,{gate:false,force:true}))}
function skip(){finish()}
window.HalteIntro={init,replay,skip,version:'1.0.0',defaults:DEF};
/* mode otomatis: <script src="halte-intro.js" data-auto></script> */
const cs=document.currentScript;
if(cs&&cs.hasAttribute('data-auto')){if(!reduce())H.classList.add('hi-pending');
 const go=()=>init();if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',go,{once:true});else go();
 setTimeout(()=>{if(!active)H.classList.remove('hi-pending')},6000)}
})();
