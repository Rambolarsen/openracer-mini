# Electronics baseline (2026-11-27)
Manufacturer-published nominal values, not physical measurements.

| Part | Envelope mm | Mount | Mass | Interface |
|---|---|---|---|---|
| AIO15 | 31.3 x 31.3 | 25.5 square M2 | 7.2 g with plugs | 2–3S, composite camera |
| Gamma | 33 x 33 | 25.5 square M2 | 8.4 g | 3–6S, 8 V / 3 A VTX rail |
| Race V3 | 28 x 32 | 20 square M4 soft | 5.5 g | 4–12 V, 5–6 W |
| Lux | 14 x 16 x 14 (LWH as listed) | measure | 2.3 g | composite |
| Nano90 V2 | 18 x 14 x 18 (LWH) | measure | 5.2 g | MIPI |

AIO15: 15 A per output continuous, 18 A peak (3 seconds). Manufacturer shop and docs disagree on 5 V BEC rating (1 A vs 3 A); use conservative 1 A pending confirmation. Input ceiling 13 V; do not assume 3S LiHV compatibility (13.05 V fully charged). Use standard 3S LiPo initially. Gamma: 45 A/60 A published; verify duration and thermal conditions. Race V3 must not be wired directly to 4S; use regulated 8 V and verify pinout and transients. Camera dimensions differ by revision; verify exact part before designing mount.

CAD measurement checklist: board height above/below PCB, grommet installed height and OD, hole coordinates, motor plug/pad envelope, battery lead/capacitor bend radius, USB access, antenna and camera cable bend/strain relief, lens protrusion and mounting screws. No measured dimensions yet. Do not release carbon from nominal envelopes alone.

Sources:
- https://www.hd-zero.com/product-page/hdzero-aio15
- https://docs.hd-zero.com/aio15-introduction
- https://docs.hd-zero.com/gamma-introduction
- https://www.hd-zero.com/product-page/hdzero-gamma-45a-hd-ready-aio
- https://hd-zero.github.io/hdzero-vtx-docs/latest/vtx_targets/
- https://docs.hd-zero.com/camera-summary
