#!/usr/bin/env python3
"""Generates the architecture diagrams as draw.io files (diagrams/drawio/<lang>/*.drawio).

C4 (context, containers) and UML (deployment, sequence, class), Truway palette.
Edit the generated .drawio files in draw.io, or change this script and run it again.
Export to PNG with scripts/render-diagrams.sh.
"""
import os, html
from xml.sax.saxutils import escape

FONT = "fontFamily=Helvetica;"
ST = {
 "person": "rounded=1;arcSize=12;whiteSpace=wrap;html=1;fillColor=#FAF5E8;strokeColor=#A58737;fontColor=#332602;fontSize=13;" + FONT,
 "system": "rounded=1;arcSize=6;whiteSpace=wrap;html=1;fillColor=#1E42D8;strokeColor=#0B1F77;fontColor=#FFFFFF;fontSize=14;" + FONT,
 "container": "rounded=1;arcSize=6;whiteSpace=wrap;html=1;fillColor=#F0F4FF;strokeColor=#243CA6;fontColor=#111318;fontSize=13;" + FONT,
 "db": "shape=cylinder3;boundedLbl=1;size=10;whiteSpace=wrap;html=1;fillColor=#F0F4FF;strokeColor=#243CA6;fontColor=#111318;fontSize=13;" + FONT,
 "chain": "rounded=1;arcSize=6;whiteSpace=wrap;html=1;fillColor=#0B1F77;strokeColor=#040B24;fontColor=#FFFFFF;fontSize=13;" + FONT,
 "external": "rounded=1;arcSize=6;whiteSpace=wrap;html=1;fillColor=#F2F2F0;strokeColor=#8F9298;fontColor=#272A30;fontSize=13;" + FONT,
 "soon": "rounded=1;arcSize=6;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#8F9298;dashed=1;fontColor=#585B62;fontSize=13;" + FONT,
 "boundary": "rounded=1;arcSize=2;whiteSpace=wrap;html=1;fillColor=none;strokeColor=#585B62;dashed=1;verticalAlign=top;align=left;spacingLeft=10;spacingTop=6;fontColor=#3F4249;fontSize=12;fontStyle=1;" + FONT,
 "node": "shape=cube;size=10;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#585B62;verticalAlign=top;align=left;spacingLeft=12;spacingTop=8;fontColor=#272A30;fontSize=12;fontStyle=1;" + FONT,
 "edge": "edgeStyle=orthogonalEdgeStyle;endArrow=block;endFill=1;html=1;strokeColor=#585B62;fontColor=#3F4249;fontSize=11;labelBackgroundColor=#FFFFFF;rounded=1;" + FONT,
 "edgesoon": "edgeStyle=orthogonalEdgeStyle;endArrow=block;endFill=1;html=1;strokeColor=#8F9298;dashed=1;fontColor=#585B62;fontSize=11;labelBackgroundColor=#FFFFFF;rounded=1;" + FONT,
 "lifeline": "shape=umlLifeline;perimeter=lifelinePerimeter;whiteSpace=wrap;html=1;container=0;collapsible=0;size=50;fillColor=#F0F4FF;strokeColor=#243CA6;fontColor=#111318;fontSize=13;" + FONT,
 "lifeperson": "shape=umlLifeline;perimeter=lifelinePerimeter;whiteSpace=wrap;html=1;container=0;collapsible=0;size=50;fillColor=#FAF5E8;strokeColor=#A58737;fontColor=#332602;fontSize=13;" + FONT,
 "lifechain": "shape=umlLifeline;perimeter=lifelinePerimeter;whiteSpace=wrap;html=1;container=0;collapsible=0;size=50;fillColor=#0B1F77;strokeColor=#040B24;fontColor=#FFFFFF;fontSize=13;" + FONT,
 "msg": "endArrow=block;endFill=1;html=1;strokeColor=#3F4249;fontColor=#111318;fontSize=11;labelBackgroundColor=#FFFFFF;align=left;verticalAlign=bottom;" + FONT,
 "ret": "endArrow=open;endFill=0;dashed=1;html=1;strokeColor=#585B62;fontColor=#3F4249;fontSize=11;labelBackgroundColor=#FFFFFF;align=left;verticalAlign=bottom;" + FONT,
 "note": "shape=note;size=12;whiteSpace=wrap;html=1;fillColor=#FAF5E8;strokeColor=#C7A667;fontColor=#332602;fontSize=11;align=left;spacingLeft=8;" + FONT,
 "classhead": "rounded=0;whiteSpace=wrap;html=1;fillColor=#1E42D8;strokeColor=#0B1F77;fontColor=#FFFFFF;fontSize=13;fontStyle=1;" + FONT,
 "classbody": "rounded=0;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#0B1F77;fontColor=#111318;fontSize=12;align=left;verticalAlign=top;spacingLeft=10;spacingTop=6;fontFamily=Menlo;",
 "enumhead": "rounded=0;whiteSpace=wrap;html=1;fillColor=#F2F2F0;strokeColor=#585B62;fontColor=#272A30;fontSize=13;fontStyle=1;" + FONT,
 "assoc": "endArrow=open;endFill=0;html=1;strokeColor=#3F4249;fontColor=#3F4249;fontSize=11;labelBackgroundColor=#FFFFFF;" + FONT,
 "comp": "shape=component;align=left;spacingLeft=36;whiteSpace=wrap;html=1;fillColor=#F0F4FF;strokeColor=#243CA6;fontColor=#111318;fontSize=12;" + FONT,
 "compchain": "shape=component;align=left;spacingLeft=36;whiteSpace=wrap;html=1;fillColor=#0B1F77;strokeColor=#040B24;fontColor=#FFFFFF;fontSize=12;" + FONT,
 "use": "edgeStyle=orthogonalEdgeStyle;endArrow=open;endFill=0;dashed=1;html=1;strokeColor=#3F4249;fontColor=#3F4249;fontSize=11;labelBackgroundColor=#FFFFFF;rounded=1;" + FONT,
 "title": "text;html=1;fontSize=18;fontStyle=1;fontColor=#111318;align=left;verticalAlign=top;" + FONT,
}

def V(label):
    return escape(label.replace("\n", "<br>"), {'"': "&quot;"})

class D:
    def __init__(self, w, h):
        self.cells = []; self.n = 2; self.w = w; self.h = h
    def box(self, kind, label, x, y, w, h):
        self.n += 1; i = f"c{self.n}"
        self.cells.append(f'<mxCell id="{i}" value="{V(label)}" style="{ST[kind]}" vertex="1" parent="1"><mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry"/></mxCell>')
        return i
    def edge(self, a, b, label="", kind="edge", pts=None, ex=None):
        self.n += 1; i = f"c{self.n}"
        style = ST[kind] + (ex or "")
        p = ""
        if pts:
            p = '<Array as="points">' + "".join(f'<mxPoint x="{x}" y="{y}"/>' for x, y in pts) + "</Array>"
        self.cells.append(f'<mxCell id="{i}" value="{V(label)}" style="{style}" edge="1" parent="1" source="{a}" target="{b}"><mxGeometry relative="1" as="geometry">{p}</mxGeometry></mxCell>')
    def msg(self, x1, x2, y, label, kind="msg"):
        self.n += 1; i = f"c{self.n}"
        self.cells.append(f'<mxCell id="{i}" value="{V(label)}" style="{ST[kind]}" edge="1" parent="1"><mxGeometry relative="1" as="geometry"><mxPoint x="{x1}" y="{y}" as="sourcePoint"/><mxPoint x="{x2}" y="{y}" as="targetPoint"/></mxGeometry></mxCell>')
    def selfmsg(self, x, y, label):
        self.n += 1; i = f"c{self.n}"
        self.cells.append(f'<mxCell id="{i}" value="{V(label)}" style="{ST["msg"]}verticalAlign=middle;" edge="1" parent="1"><mxGeometry relative="1" as="geometry"><mxPoint x="{x}" y="{y}" as="sourcePoint"/><mxPoint x="{x}" y="{y+22}" as="targetPoint"/><Array as="points"><mxPoint x="{x+40}" y="{y}"/><mxPoint x="{x+40}" y="{y+22}"/></Array></mxGeometry></mxCell>')
    def xml(self, name):
        body = "".join(self.cells)
        return (f'<mxfile host="drawio"><diagram name="{escape(name)}" id="{escape(name)}"><mxGraphModel dx="1200" dy="800" grid="0" gridSize="10" '
                f'guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="0" pageScale="1" pageWidth="{self.w}" pageHeight="{self.h}" background="#FFFFFF" math="0" shadow="0">'
                f'<root><mxCell id="0"/><mxCell id="1" parent="0"/>{body}</root></mxGraphModel></diagram></mxfile>')

def c4(name, kind, desc):
    return f"<b>{name}</b><br><font style='font-size:11px'>[{kind}]</font><br><br>{desc}"

def context(L):
    d = D(1300, 860)
    p = [d.box("person", c4(*L["p1"]), 40, 40, 250, 120), d.box("person", c4(*L["p2"]), 360, 40, 250, 120),
         d.box("person", c4(*L["p3"]), 680, 40, 250, 120), d.box("person", c4(*L["p4"]), 1000, 40, 250, 120)]
    t = d.box("system", c4(*L["truway"]), 460, 330, 380, 150)
    e = [d.box("chain", c4(*L["stellar"]), 40, 640, 260, 140), d.box("external", c4(*L["wa"]), 340, 640, 220, 140),
         d.box("external", c4(*L["privy"]), 600, 640, 200, 140), d.box("external", c4(*L["gemini"]), 840, 640, 200, 140),
         d.box("soon", c4(*L["secop"]), 1080, 640, 190, 140)]
    for src, lab, ex in zip(p, L["pedges"], [0.15, 0.38, 0.62, 0.85]):
        d.edge(src, t, lab, ex=f"edgeStyle=none;exitX=0.5;exitY=1;entryX={ex};entryY=0;")
    for dst, lab, k, ex in zip(e, L["eedges"], ["edge", "edge", "edge", "edge", "edgesoon"], [0.08, 0.3, 0.5, 0.7, 0.92]):
        d.edge(t, dst, lab, k, ex=f"edgeStyle=none;exitX={ex};exitY=1;entryX=0.5;entryY=0;")
    return d

def containers(L):
    d = D(1420, 980)
    org = d.box("person", c4(*L["org"]), 60, 30, 280, 110)
    vee = d.box("person", c4(*L["vee"]), 420, 30, 280, 110)
    fld = d.box("person", c4(*L["fld"]), 1080, 30, 280, 110)
    d.box("boundary", L["bTruway"], 30, 190, 990, 520)
    web = d.box("container", c4(*L["web"]), 60, 240, 280, 130)
    api = d.box("container", c4(*L["api"]), 420, 240, 340, 150)
    db = d.box("db", c4(*L["db"]), 60, 520, 260, 150)
    rq = d.box("db", c4(*L["rq"]), 420, 520, 240, 150)
    st = d.box("db", c4(*L["st"]), 730, 520, 260, 150)
    wa = d.box("external", c4(*L["wa"]), 1080, 240, 280, 110)
    pv = d.box("external", c4(*L["privy"]), 1080, 400, 280, 110)
    gm = d.box("external", c4(*L["gemini"]), 1080, 560, 280, 110)
    d.box("boundary", L["bStellar"], 30, 760, 1330, 190)
    rpc = d.box("chain", c4(*L["rpc"]), 60, 810, 300, 120)
    bt = d.box("chain", c4(*L["bt"]), 520, 810, 360, 120)
    sac = d.box("chain", c4(*L["sac"]), 1040, 810, 300, 120)
    E = L["edges"]
    d.edge(org, web, E[0]); d.edge(vee, web, E[1], ex="exitX=0.5;exitY=1;entryX=0.75;entryY=0;"); d.edge(fld, wa, E[2])
    d.edge(web, api, E[3]); d.edge(wa, api, E[4], ex="exitX=0;exitY=0.5;entryX=1;entryY=0.3;")
    d.edge(api, db, E[5], ex="exitX=0.15;exitY=1;entryX=0.5;entryY=0;"); d.edge(api, rq, E[6], ex="exitX=0.45;exitY=1;entryX=0.5;entryY=0;")
    d.edge(api, st, E[7], ex="exitX=0.85;exitY=1;entryX=0.5;entryY=0;")
    d.edge(api, pv, E[8], pts=[(1040, 337), (1040, 455)], ex="exitX=1;exitY=0.65;entryX=0;entryY=0.5;")
    d.edge(api, gm, E[9], pts=[(1055, 375), (1055, 615)], ex="exitX=1;exitY=0.9;entryX=0;entryY=0.5;")
    d.edge(api, rpc, E[10], pts=[(380, 450), (380, 730), (210, 730)], ex="exitX=0;exitY=0.85;entryX=0.5;entryY=0;")
    d.edge(rpc, bt, E[11]); d.edge(bt, sac, E[12], "edgesoon")
    return d

def deployment(L):
    d = D(1400, 900)
    dev = d.box("node", L["devices"], 30, 40, 260, 230)
    d.box("container", L["browser"], 55, 90, 210, 60); d.box("container", L["phone"], 55, 180, 210, 60)
    cf = d.box("node", L["cf"], 340, 40, 300, 230)
    dns = d.box("external", L["dns"], 365, 90, 250, 60); pages = d.box("external", L["pages"], 365, 180, 250, 60)
    cloud = d.box("node", L["cloud"], 340, 330, 640, 270)
    appn = d.box("node", L["appsrv"], 365, 380, 280, 190)
    d.box("container", L["nextjs"], 390, 440, 230, 90)
    apin = d.box("node", L["apisrv"], 675, 380, 280, 190)
    d.box("container", L["nest"], 700, 440, 230, 90)
    man = d.box("node", L["managed"], 1030, 330, 340, 270)
    pg = d.box("db", "PostgreSQL", 1060, 380, 130, 90); rd = d.box("db", "Redis", 1210, 380, 130, 90)
    ob = d.box("db", L["objects"], 1110, 490, 180, 90)
    saas = d.box("node", L["saas"], 700, 40, 670, 230)
    pv = d.box("external", "Privy", 725, 100, 140, 60); gm = d.box("external", "Google Gemini", 885, 100, 160, 60)
    mt = d.box("external", "WhatsApp Cloud API\n(Meta)", 1065, 100, 180, 60)
    stl = d.box("node", L["stellarnode"], 340, 650, 1030, 210)
    rpc = d.box("chain", "Stellar RPC", 370, 720, 220, 90)
    bt = d.box("chain", L["btnode"], 640, 720, 360, 90)
    sac = d.box("chain", "USDC\nStellar Asset Contract", 1050, 720, 280, 90)
    E = L["edges"]
    d.edge(dev, dns, E[0]); d.edge(dns, pages, E[1]); d.edge(dns, appn, E[2], pts=[(345, 120), (345, 300), (495, 300)], ex="exitX=0;exitY=0.5;entryX=0.5;entryY=0;")
    d.edge(dns, apin, E[3], pts=[(630, 300), (815, 300)]); d.edge(appn, apin, E[4])
    d.edge(apin, man, E[5]); d.edge(apin, gm, E[6], pts=[(965, 360), (965, 290), (965, 175)], ex="exitX=1;exitY=0;")
    d.edge(mt, apin, E[7], pts=[(1155, 300), (900, 300)]); d.edge(dev, pv, E[8], pts=[(160, 15), (795, 15)], ex="exitX=0.5;exitY=0;entryX=0.5;entryY=0;")
    d.edge(apin, rpc, E[9], pts=[(815, 630), (480, 630)]); d.edge(rpc, bt, E[10]); d.edge(bt, sac, E[11], "edgesoon")
    return d

def sequence(L):
    d = D(1500, 1000)
    xs = [40, 270, 500, 760, 1010, 1260]; names = L["actors"]; kinds = L.get("kinds", ["lifeperson", "lifeline", "lifeline", "lifeperson", "lifechain", "lifeline"])
    for x, n, k in zip(xs, names, kinds):
        d.box(k, n, x, 20, 200, 940)
    cx = [x + 100 for x in xs]
    y = 110
    for step in L["steps"]:
        t = step[0]
        if t == "m": d.msg(cx[step[1]], cx[step[2]], y, step[3]); y += 52
        elif t == "r": d.msg(cx[step[1]], cx[step[2]], y, step[3], "ret"); y += 52
        elif t == "s": d.selfmsg(cx[step[1]], y, step[2]); y += 62
        elif t == "n": d.box("note", step[3], min(cx[step[1]], cx[step[2]]) - 90, y - 12, abs(cx[step[2]] - cx[step[1]]) + 180, 44); y += 60
    return d

def classes(L):
    d = D(1260, 800)
    def cls(head, body, x, y, w, hb, kind="classhead"):
        h = d.box(kind, head, x, y, w, 36); b = d.box("classbody", html.escape(body), x, y + 36, w, hb); return h, b
    tr = cls("Treasury", "+ token: Address\n+ token_symbol: Symbol\n+ members: Map<Address, Role>\n+ next_id: u64\n\n+ fund(from, project, source, amount): i128\n+ propose(proposer, action): u64\n+ approve(approver, id)\n+ reject(member, id)", 420, 20, 460, 200)
    ro = cls("«enum» Role", "Admin · Approver · Operator", 40, 100, 300, 44, "enumhead")
    bl = cls("BudgetLine", "+ project: BytesN<32>\n+ line: BytesN<32>\n+ source: BytesN<32>\n+ chart: Symbol\n+ account: Symbol\n+ currency: Symbol\n+ budget: i128\n+ paid: i128   {paid <= budget}", 20, 340, 380, 190)
    fu = cls("Funds", "+ project: BytesN<32>\n+ source: BytesN<32>\n+ amount: i128", 450, 340, 300, 80)
    pr = cls("Proposal", "+ id: u64\n+ proposer: Address\n+ action: Action\n+ status: ProposalStatus\n+ decided_by: Option<Address>\n+ created_at: u64\n+ decided_at: u64", 840, 340, 400, 170)
    st = cls("«enum» ProposalStatus", "Pending · Executed · Rejected", 450, 500, 300, 44, "enumhead")
    ac = cls("«enum» Action", "SetBudget · RecordExpense · Pay\nAddMember · RemoveMember · Upgrade", 420, 640, 360, 64, "enumhead")
    rc = cls("Receipt", "+ receipt_hash: BytesN<32>\n+ proposal_id: u64", 880, 640, 320, 64)
    ex = "edgeStyle=none;"
    d.edge(tr[1], ro[0], "members", "assoc", ex=ex + "exitX=0;exitY=0.4;entryX=1;entryY=0.5;")
    d.edge(tr[1], bl[0], L["lines"], "assoc", ex=ex + "exitX=0.15;exitY=1;entryX=0.5;entryY=0;")
    d.edge(tr[1], fu[0], L["funds"], "assoc", ex=ex + "exitX=0.45;exitY=1;entryX=0.5;entryY=0;")
    d.edge(tr[1], pr[0], L["proposals"], "assoc", ex=ex + "exitX=0.85;exitY=1;entryX=0.5;entryY=0;")
    d.edge(pr[1], st[0], "status", "assoc", ex=ex + "exitX=0;exitY=0.85;entryX=1;entryY=0.5;")
    d.edge(pr[1], ac[0], "action", "assoc", ex=ex + "exitX=0.2;exitY=1;entryX=1;entryY=0.3;")
    d.edge(pr[1], rc[0], L["uses"], "assoc", ex=ex + "exitX=0.6;exitY=1;entryX=0.5;entryY=0;")
    return d

def components(L):
    d = D(1400, 900)
    d.box("boundary", L["bApp"], 20, 40, 300, 360)
    panel = d.box("comp", L["panel"], 40, 90, 260, 70)
    explo = d.box("comp", L["explorer"], 40, 190, 260, 70)
    signer = d.box("comp", L["signer"], 40, 290, 260, 70)
    d.box("boundary", L["bApi"], 360, 40, 640, 560)
    auth = d.box("comp", L["auth"], 380, 90, 290, 70)
    prog = d.box("comp", L["prog"], 380, 190, 290, 70)
    proof = d.box("comp", L["proof"], 380, 290, 290, 70)
    stor = d.box("comp", L["storage"], 380, 390, 290, 70)
    cap = d.box("comp", L["capture"], 700, 90, 280, 70)
    ai = d.box("comp", L["ai"], 700, 190, 280, 70)
    tre = d.box("comp", L["treasury"], 700, 290, 280, 70)
    chain = d.box("comp", L["chain"], 700, 390, 280, 70)
    idx = d.box("comp", L["indexer"], 700, 500, 280, 70)
    wa = d.box("external", L["wa"], 1060, 90, 300, 70)
    gm = d.box("external", "Google Gemini", 1060, 190, 300, 70)
    pv = d.box("external", "Privy", 40, 460, 260, 70)
    d.box("boundary", "Stellar", 1040, 330, 340, 380)
    rpc = d.box("chain", "Stellar RPC", 1060, 380, 300, 70)
    bt = d.box("compchain", L["bt"], 1060, 500, 300, 70)
    sac = d.box("compchain", "USDC · Stellar Asset Contract", 1060, 610, 300, 70)
    pg = d.box("db", "PostgreSQL", 380, 680, 200, 110)
    rd = d.box("db", "Redis", 620, 680, 180, 110)
    ob = d.box("db", L["objects"], 840, 680, 200, 110)
    u = "use"
    d.edge(panel, prog, "", u, ex="exitX=1;exitY=0.5;entryX=0;entryY=0.5;")
    d.edge(panel, auth, "", u, ex="exitX=1;exitY=0.3;entryX=0;entryY=0.5;")
    d.edge(explo, proof, "", u, ex="exitX=1;exitY=0.5;entryX=0;entryY=0.5;")
    d.edge(signer, pv, "SDK", u, ex="exitX=0.5;exitY=1;entryX=0.5;entryY=0;")
    d.edge(wa, cap, "webhooks", u, ex="exitX=0;exitY=0.5;entryX=1;entryY=0.5;")
    d.edge(cap, ai, "", u, ex="exitX=0.5;exitY=1;entryX=0.5;entryY=0;")
    d.edge(ai, gm, "", u, ex="exitX=1;exitY=0.5;entryX=0;entryY=0.5;")
    d.edge(cap, stor, "", u, ex="exitX=0;exitY=0.8;entryX=1;entryY=0.3;", pts=[(685, 146), (685, 411)])
    d.edge(prog, tre, "", u, ex="exitX=1;exitY=0.8;entryX=0;entryY=0.3;")
    d.edge(tre, chain, "", u, ex="exitX=0.5;exitY=1;entryX=0.5;entryY=0;")
    d.edge(idx, chain, "", u, ex="exitX=0.5;exitY=0;entryX=0.5;entryY=1;")
    d.edge(chain, rpc, L["bindings"], u, ex="exitX=1;exitY=0.4;entryX=0;entryY=0.5;")
    d.edge(rpc, bt, "", "edge", ex="exitX=0.5;exitY=1;entryX=0.5;entryY=0;")
    d.edge(bt, sac, "", "edgesoon", ex="exitX=0.5;exitY=1;entryX=0.5;entryY=0;")
    d.edge(prog, pg, "", u, ex="exitX=0.2;exitY=1;entryX=0.2;entryY=0;", pts=[(438, 270), (438, 640), (420, 640)])
    d.edge(proof, pg, "", u, ex="exitX=0.4;exitY=1;entryX=0.5;entryY=0;", pts=[(496, 640), (480, 640)])
    d.edge(idx, pg, "", u, ex="exitX=0;exitY=0.7;entryX=0.8;entryY=0;", pts=[(560, 549), (560, 660), (540, 660)])
    d.edge(idx, rd, "", u, ex="exitX=0.3;exitY=1;entryX=0.5;entryY=0;")
    d.edge(stor, ob, "", u, ex="exitX=1;exitY=0.8;entryX=0.5;entryY=0;", pts=[(690, 446), (690, 620), (940, 620)])
    return d

def web3(L):
    d = D(1500, 900)
    mem = d.box("person", c4(*L["members"]), 30, 60, 260, 120)
    d.box("boundary", L["bOff"], 20, 220, 300, 440)
    api = d.box("container", c4(*L["api"]), 40, 270, 260, 120)
    sub = d.box("container", L["submitter"], 40, 420, 260, 60)
    dep = d.box("container", L["deployer"], 40, 500, 260, 60)
    idx = d.box("container", L["indexer"], 40, 580, 260, 60)
    d.box("boundary", L["bNet"], 380, 40, 720, 760)
    rpc = d.box("chain", c4(*L["rpc"]), 410, 290, 240, 120)
    led = d.box("chain", c4(*L["ledger"]), 410, 520, 240, 110)
    wasm = d.box("external", L["wasm"], 760, 80, 310, 80)
    bta = d.box("chain", c4(*L["bta"]), 760, 220, 310, 120)
    btb = d.box("chain", c4(*L["btb"]), 760, 380, 310, 100)
    sac = d.box("chain", c4(*L["sac"]), 760, 530, 310, 100)
    reg = d.box("soon", L["registry"], 760, 690, 310, 70)
    gh = d.box("external", L["release"], 1160, 80, 300, 80)
    se = d.box("external", L["explorers"], 1160, 280, 300, 90)
    rd = d.box("person", c4(*L["readers"]), 1160, 420, 300, 110)
    sdp = d.box("soon", L["sdp"], 1160, 600, 300, 70)
    anc = d.box("soon", L["anchor"], 1160, 720, 300, 70)
    E = L["edges"]; n = "edgeStyle=none;"
    d.edge(mem, api, E[0], ex=n + "exitX=0.5;exitY=1;entryX=0.5;entryY=0;")
    d.edge(api, rpc, E[1], ex=n + "exitX=1;exitY=0.5;entryX=0;entryY=0.35;")
    d.edge(sub, rpc, E[2], ex=n + "exitX=1;exitY=0.3;entryX=0;entryY=0.8;")
    d.edge(rpc, bta, E[3], ex=n + "exitX=1;exitY=0.25;entryX=0;entryY=0.5;")
    d.edge(rpc, btb, "", ex=n + "exitX=1;exitY=0.6;entryX=0;entryY=0.3;")
    d.edge(wasm, bta, E[4], ex=n + "exitX=0.5;exitY=1;entryX=0.5;entryY=0;")
    d.edge(dep, wasm, E[5], ex="exitX=1;exitY=0.3;entryX=0;entryY=0.5;", pts=[(345, 518), (345, 120)])
    d.edge(btb, led, E[6], ex=n + "exitX=0;exitY=0.85;entryX=1;entryY=0.3;")
    d.edge(idx, led, E[7], ex=n + "exitX=1;exitY=0.5;entryX=0;entryY=0.6;")
    d.edge(btb, sac, E[8], "edgesoon", ex=n + "exitX=0.5;exitY=1;entryX=0.5;entryY=0;")
    d.edge(btb, reg, E[12], "edgesoon", ex="exitX=1;exitY=0.5;entryX=1;entryY=0.5;", pts=[(1085, 430), (1085, 725)])
    d.edge(gh, wasm, E[9], ex=n + "exitX=0;exitY=0.5;entryX=1;entryY=0.5;")
    d.edge(se, gh, E[10], ex=n + "exitX=0.5;exitY=0;entryX=0.5;entryY=1;")
    d.edge(se, led, E[11], ex="exitX=0;exitY=0.7;entryX=0.5;entryY=1;", pts=[(1130, 343), (1130, 830), (530, 830)])
    d.edge(rd, se, "", ex=n + "exitX=0.5;exitY=0;entryX=0.5;entryY=1;")
    d.edge(sac, sdp, E[13], "edgesoon", ex="exitX=1;exitY=0.7;entryX=0;entryY=0.5;")
    d.edge(sdp, anc, E[14], "edgesoon", ex=n + "exitX=0.5;exitY=1;entryX=0.5;entryY=0;")
    return d

ES = dict(
 ctx=dict(p1=("Supervisor", "Persona", "De la entidad pública. Aprueba rubros y gastos."), p2=("Coordinación", "Persona", "De la organización ejecutora. Asigna anticipos y propone gastos."),
  p3=("Equipo de campo", "Persona", "Paga en campo y envía los recibos."), p4=("Veedor o ciudadano", "Persona", "Verifica gastos sin cuenta."),
  truway=("Truway", "Sistema", "Ejecución presupuestal verificable: rubros, anticipos, gastos con doble aprobación e informes."),
  stellar=("Stellar", "Sistema externo", "Contrato budget-treasury por organización y ledger público."), wa=("WhatsApp Business", "Sistema externo", "Canal de captura de recibos."),
  privy=("Privy", "Sistema externo", "Inicio de sesión y firmante integrado."), gemini=("Google Gemini", "Sistema externo", "Lee los datos de las facturas."),
  secop=("SECOP II", "Sistema externo", "Contratos públicos. Próximamente."),
  pedges=["Aprueba [web]", "Asigna y propone [web]", "Envía recibos [WhatsApp]", "Verifica [web, sin cuenta]"],
  eedges=["Propuestas y aprobaciones firmadas;\nlee eventos [RPC]", "Mensajes [Cloud API]", "Sesión y firma [SDK]", "Extrae datos [API]", "Lee contratos [datos abiertos]"],
  direct="Lee el registro sin Truway"),
 cont=dict(org=("Personas de la organización", "Persona", "Coordinación, aprobadores y supervisor."), vee=("Veedor o ciudadano", "Persona", "Verifica gastos sin cuenta."),
  fld=("Equipo de campo", "Persona", "Envía recibos por WhatsApp."), bTruway="Truway [límite del sistema]",
  web=("App web", "Contenedor: Next.js 16", "Panel, aprobaciones, explorador público."), api=("API", "Contenedor: NestJS 11 y BullMQ", "Lógica de negocio, captura, tesorería e indexador de eventos cada 15 s. Arma cada transacción para quien firma y paga la comisión."),
  job=("Trabajos en segundo plano", "Contenedor: BullMQ", "Indexador de eventos cada 15 s y envíos en cola."),
  db=("Base de datos", "Contenedor: PostgreSQL", "Programas, personas, eventos indexados."), rq=("Colas", "Contenedor: Redis", "Trabajos y sesiones del bot."),
  st=("Almacenamiento de soportes", "Contenedor: objetos", "Facturas y recibos privados."),
  wa=("WhatsApp Cloud API", "Sistema externo", "Mensajes del bot."), privy=("Privy", "Sistema externo", "Sesión y firmante integrado."), gemini=("Google Gemini", "Sistema externo", "Lectura de facturas."),
  bStellar="Stellar [red pública]", rpc=("Stellar RPC", "Servicio", "Simula, envía y lee eventos."), bt=("budget-treasury", "Contrato Soroban, uno por organización", "Reglas: dos firmantes, rubros, soporte único."),
  sac=("USDC", "Stellar Asset Contract", "Activo de la tesorería."),
  edges=["Usa [HTTPS]", "Verifica [HTTPS]", "Envía recibos", "JSON/HTTPS", "Webhooks", "SQL", "Colas", "Archivos", "Sesión", "Lectura", "simulate, send, getEvents", "Invoca", "fund y Pay"]),
 dep=dict(devices="«dispositivo»\nPersonas", browser="Navegador", phone="Celular con WhatsApp", cf="«nube» Cloudflare", dns="DNS truway.xyz", pages="Sitio web\nCloudflare Pages",
  cloud="«nube» Proveedor de nube", appsrv="«servidor» App", nextjs="Next.js\napp.truway.xyz", apisrv="«servidor» API", nest="NestJS y workers\napi.truway.xyz",
  managed="«servicios administrados»", objects="Almacenamiento\nde objetos", saas="«servicios externos»", docs="documentación",
  stellarnode="«red» Stellar testnet", btnode="budget-treasury\nuna instancia por organización",
  edges=["HTTPS", "truway.xyz", "app.truway.xyz", "api.truway.xyz", "HTTPS", "SQL, colas, archivos", "API", "webhooks", "SDK", "RPC", "invoca", "fund y Pay"]),
 seq=dict(actors=["Líder del equipo", "WhatsApp", "API de Truway", "Aprobador", "budget-treasury", "Indexador"],
  steps=[("m",0,1,"1. Foto del recibo"),("m",1,2,"2. Webhook con la imagen"),("s",2,"3. Guarda el archivo y calcula SHA-256"),("s",2,"4. La IA lee valor, proveedor, fecha y NIT"),
         ("r",2,0,"5. ¿A qué rubro pertenece?"),("m",0,2,"6. Número del rubro"),("m",2,4,"7. propose(RecordExpense), firmado por la líder"),
         ("n",2,4,"En testnet firma un firmante de demostración; Truway paga la comisión"),("r",4,2,"8. proposal_created"),("m",3,2,"9. Aprobar"),
         ("m",2,4,"10. approve(id), firmado por el aprobador"),("n",4,4,"Revisa rol, rubro, saldo y soporte sin usar"),("r",4,2,"11. expense_recorded y proposal_executed"),
         ("m",5,4,"12. getEvents cada 15 s"),("r",5,2,"13. Guarda los eventos")]),
 comp=dict(bApp="«componente» App web · Next.js 16", panel="Panel y aprobaciones", explorer="Explorador público\n/proof", signer="Firmante integrado\n(Privy SDK)",
  bApi="«componente» API · NestJS 11", auth="Identidad y permisos\nAuthModule", prog="Programas y presupuesto\nProjectsModule", proof="Prueba pública\nPublicProofService",
  storage="Almacenamiento de soportes\nStorageService", capture="Captura por WhatsApp\nWhatsAppModule", ai="Lectura de facturas\nGeminiService", treasury="Tesorería\nTreasuryService",
  chain="Cliente Soroban\nTreasuryChainService", indexer="Indexador\ncola treasury-ops · 15 s", wa="WhatsApp Cloud API", bt="budget-treasury\nuna instancia por organización",
  objects="Almacenamiento\nde objetos", bindings="bindings TypeScript"),
 w3=dict(members=("Miembros de la organización", "Persona", "Cada uno con su cuenta Stellar, guardada por Privy."), bOff="Fuera de la red", api=("API de Truway", "NestJS", "Arma la invocación y pide la firma de cada miembro."),
  submitter="Cuenta remitente de Truway\npaga comisiones y envía", deployer="Cuenta de despliegue\nun solo uso, nunca es miembro", indexer="Indexador\ngetEvents cada 15 s",
  bNet="Stellar testnet", rpc=("Stellar RPC", "Servicio", "simulateTransaction, sendTransaction, getEvents"), wasm="WASM budget-treasury 0.4.0\nhash 183dd156…  ·  event_schema = proof-of-spend/1",
  bta=("budget-treasury · Organización A", "Contrato Soroban", "Miembros, rubros, fondos, propuestas, soportes usados."), btb=("budget-treasury · Organización B", "Contrato Soroban", "Misma lógica, otra instancia."),
  sac=("USDC", "Stellar Asset Contract (SEP-41)", "Activo de la tesorería."), ledger=("Ledger público", "Eventos Proof of Spend", "budget_set, expense_recorded, proposal_executed…"),
  registry="Registro compartido de soportes\npróximamente", release="Release en GitHub\nWASM atestado (SEP-55)", explorers="Stellar Expert y Stellar Lab\nmuestran el commit de origen",
  readers=("Lectores", "Persona", "Financiadores, auditores, entes de control, cualquiera."), sdp="Stellar Disbursement Platform\nanticipos · próximamente", anchor="Anchor a pesos (SEP-24/31)\nbanco o Bre-B · próximamente",
  edges=["firma su entrada de autorización\n(signRawHash)", "invocación firmada", "sobre de la transacción\n(fee sponsorship)", "propose / approve", "código", "despliega", "eventos", "getEvents", "fund y Pay", "atesta", "lee la atestación", "lee", "soporte único", "anticipo", "salida a pesos"]),
 sig=dict(kinds=["lifeperson", "lifeline", "lifeline", "lifechain", "lifechain", "lifechain"], actors=["Miembro (navegador)", "Privy", "API de Truway", "Stellar RPC", "budget-treasury", "Ledger"],
  steps=[("m",0,2,"1. Aprobar"),("m",2,3,"2. simulateTransaction(approve)"),("r",3,2,"3. Entrada de autorización del miembro"),("s",2,"4. Fija nonce y vencimiento (~720 ledgers)"),
         ("r",2,0,"5. Hash a firmar"),("m",0,1,"6. signRawHash"),("r",1,0,"7. Firma"),("m",0,2,"8. Firma"),("s",2,"9. Verifica la firma con la dirección del miembro"),
         ("m",2,3,"10. sendTransaction: origen y comisión de Truway"),("n",2,3,"El servidor no puede cambiar lo firmado ni firmar por el miembro"),("m",3,4,"11. approve(approver, id)"),
         ("s",4,"12. require_auth del miembro; reglas del contrato"),("m",4,5,"13. proposal_executed"),("r",2,0,"14. Registrado · verificable")]),
 cls=dict(lines="1  →  * líneas", funds="1  →  * fondos", proposals="1  →  * propuestas", uses="0..1  usa"),
)
EN = dict(
 ctx=dict(p1=("Supervisor", "Person", "From the government agency. Approves budget lines and expenses."), p2=("Coordinator", "Person", "From the executing organization. Assigns advances and proposes expenses."),
  p3=("Field team", "Person", "Pays in the field and sends receipts."), p4=("Oversight group or citizen", "Person", "Verifies expenses without an account."),
  truway=("Truway", "Software System", "Verifiable budget execution: budget lines, advances, two-person approved expenses and reports."),
  stellar=("Stellar", "External System", "One budget-treasury contract per organization and the public ledger."), wa=("WhatsApp Business", "External System", "Receipt capture channel."),
  privy=("Privy", "External System", "Sign-in and embedded signer."), gemini=("Google Gemini", "External System", "Reads invoice data."),
  secop=("SECOP II", "External System", "Public contracts. Coming soon."),
  pedges=["Approves [web]", "Assigns and proposes [web]", "Sends receipts [WhatsApp]", "Verifies [web, no account]"],
  eedges=["Signed proposals and approvals;\nreads events [RPC]", "Messages [Cloud API]", "Session and signing [SDK]", "Extracts data [API]", "Reads contracts [open data]"],
  direct="Reads the record without Truway"),
 cont=dict(org=("Organization people", "Person", "Coordinator, approvers and supervisor."), vee=("Oversight group or citizen", "Person", "Verifies expenses without an account."),
  fld=("Field team", "Person", "Sends receipts over WhatsApp."), bTruway="Truway [system boundary]",
  web=("Web app", "Container: Next.js 16", "Dashboard, approvals, public explorer."), api=("API", "Container: NestJS 11 and BullMQ", "Business logic, capture, treasury and an event indexer every 15 s. Builds each transaction for the signer and pays the fee."),
  job=("Background jobs", "Container: BullMQ", "Event indexer every 15 s and queued submissions."),
  db=("Database", "Container: PostgreSQL", "Programs, people, indexed events."), rq=("Queues", "Container: Redis", "Jobs and bot sessions."),
  st=("Document storage", "Container: object storage", "Private invoices and receipts."),
  wa=("WhatsApp Cloud API", "External System", "Bot messages."), privy=("Privy", "External System", "Session and embedded signer."), gemini=("Google Gemini", "External System", "Invoice reading."),
  bStellar="Stellar [public network]", rpc=("Stellar RPC", "Service", "Simulates, submits and reads events."), bt=("budget-treasury", "Soroban contract, one per organization", "Rules: two signers, budget lines, single-use documents."),
  sac=("USDC", "Stellar Asset Contract", "Treasury asset."),
  edges=["Uses [HTTPS]", "Verifies [HTTPS]", "Sends receipts", "JSON/HTTPS", "Webhooks", "SQL", "Queues", "Files", "Session", "Reading", "simulate, send, getEvents", "Invokes", "fund and Pay"]),
 dep=dict(devices="«device»\nPeople", browser="Browser", phone="Phone with WhatsApp", cf="«cloud» Cloudflare", dns="truway.xyz DNS", pages="Website\nCloudflare Pages",
  cloud="«cloud» Cloud provider", appsrv="«server» App", nextjs="Next.js\napp.truway.xyz", apisrv="«server» API", nest="NestJS and workers\napi.truway.xyz",
  managed="«managed services»", objects="Object\nstorage", saas="«external services»", docs="documentation",
  stellarnode="«network» Stellar testnet", btnode="budget-treasury\none instance per organization",
  edges=["HTTPS", "truway.xyz", "app.truway.xyz", "api.truway.xyz", "HTTPS", "SQL, queues, files", "API", "webhooks", "SDK", "RPC", "invokes", "fund and Pay"]),
 seq=dict(actors=["Team lead", "WhatsApp", "Truway API", "Approver", "budget-treasury", "Indexer"],
  steps=[("m",0,1,"1. Receipt photo"),("m",1,2,"2. Webhook with the image"),("s",2,"3. Stores the file, computes SHA-256"),("s",2,"4. AI reads amount, supplier, date, tax ID"),
         ("r",2,0,"5. Which budget line is it?"),("m",0,2,"6. Budget line number"),("m",2,4,"7. propose(RecordExpense), signed by the team lead"),
         ("n",2,4,"On testnet a demo signer signs; Truway pays the fee"),("r",4,2,"8. proposal_created"),("m",3,2,"9. Approve"),
         ("m",2,4,"10. approve(id), signed by the approver"),("n",4,4,"Checks role, line, room left, unused document"),("r",4,2,"11. expense_recorded and proposal_executed"),
         ("m",5,4,"12. getEvents every 15 s"),("r",5,2,"13. Stores the events")]),
 comp=dict(bApp="«component» Web app · Next.js 16", panel="Dashboard and approvals", explorer="Public explorer\n/proof", signer="Embedded signer\n(Privy SDK)",
  bApi="«component» API · NestJS 11", auth="Identity and permissions\nAuthModule", prog="Programs and budget\nProjectsModule", proof="Public proof\nPublicProofService",
  storage="Document storage\nStorageService", capture="WhatsApp capture\nWhatsAppModule", ai="Invoice reading\nGeminiService", treasury="Treasury\nTreasuryService",
  chain="Soroban client\nTreasuryChainService", indexer="Indexer\ntreasury-ops queue · 15 s", wa="WhatsApp Cloud API", bt="budget-treasury\none instance per organization",
  objects="Object\nstorage", bindings="TypeScript bindings"),
 w3=dict(members=("Organization members", "Person", "Each with their own Stellar account, held by Privy."), bOff="Off the ledger", api=("Truway API", "NestJS", "Builds the invocation and asks each member to sign."),
  submitter="Truway submitter account\npays fees and submits", deployer="Deployer account\nsingle use, never a member", indexer="Indexer\ngetEvents every 15 s",
  bNet="Stellar testnet", rpc=("Stellar RPC", "Service", "simulateTransaction, sendTransaction, getEvents"), wasm="budget-treasury WASM 0.4.0\nhash 183dd156…  ·  event_schema = proof-of-spend/1",
  bta=("budget-treasury · Organization A", "Soroban contract", "Members, budget lines, funds, proposals, used documents."), btb=("budget-treasury · Organization B", "Soroban contract", "Same logic, another instance."),
  sac=("USDC", "Stellar Asset Contract (SEP-41)", "Treasury asset."), ledger=("Public ledger", "Proof of Spend events", "budget_set, expense_recorded, proposal_executed…"),
  registry="Shared document registry\ncoming soon", release="GitHub release\nattested WASM (SEP-55)", explorers="Stellar Expert and Stellar Lab\nshow the source commit",
  readers=("Readers", "Person", "Funders, auditors, oversight bodies, anyone."), sdp="Stellar Disbursement Platform\nadvances · coming soon", anchor="Anchor to pesos (SEP-24/31)\nbank or Bre-B · coming soon",
  edges=["signs their authorization entry\n(signRawHash)", "signed invocation", "transaction envelope\n(fee sponsorship)", "propose / approve", "code", "deploys", "events", "getEvents", "fund and Pay", "attests", "reads the attestation", "reads", "single-use document", "advance", "cash-out"]),
 sig=dict(kinds=["lifeperson", "lifeline", "lifeline", "lifechain", "lifechain", "lifechain"], actors=["Member (browser)", "Privy", "Truway API", "Stellar RPC", "budget-treasury", "Ledger"],
  steps=[("m",0,2,"1. Approve"),("m",2,3,"2. simulateTransaction(approve)"),("r",3,2,"3. Member's authorization entry"),("s",2,"4. Sets nonce and expiry (~720 ledgers)"),
         ("r",2,0,"5. Hash to sign"),("m",0,1,"6. signRawHash"),("r",1,0,"7. Signature"),("m",0,2,"8. Signature"),("s",2,"9. Checks the signature against the member's address"),
         ("m",2,3,"10. sendTransaction: Truway is source and fee payer"),("n",2,3,"The server cannot change what was signed or sign for the member"),("m",3,4,"11. approve(approver, id)"),
         ("s",4,"12. Member's require_auth; contract rules"),("m",4,5,"13. proposal_executed"),("r",2,0,"14. Registered · verifiable")]),
 cls=dict(lines="1  →  * lines", funds="1  →  * funds", proposals="1  →  * proposals", uses="0..1  uses"),
)
NAMES = {"es": ["c4-contexto", "componentes", "despliegue", "arquitectura-stellar", "secuencia-gasto", "secuencia-firma", "clases-contrato"],
         "en": ["c4-context", "components", "deployment", "stellar-architecture", "expense-sequence", "signing-sequence", "contract-classes"]}
if __name__ == "__main__":
    root = os.path.join(os.path.dirname(__file__), "..", "diagrams", "drawio")
    for lang, L in (("es", ES), ("en", EN)):
        os.makedirs(os.path.join(root, lang), exist_ok=True)
        ds = [context(L["ctx"]), components(L["comp"]), deployment(L["dep"]), web3(L["w3"]), sequence(L["seq"]), sequence(L["sig"]), classes(L["cls"])]
        for name, d in zip(NAMES[lang], ds):
            open(os.path.join(root, lang, name + ".drawio"), "w").write(d.xml(name))
            print("wrote", lang, name)
