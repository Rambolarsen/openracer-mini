# Upstream-first adaptation
Decision: supersede R0/R1 bespoke guide concepts. Derive from OpenRacer rather than redesigning its retention. Preserve sandwich plates, two arm-retaining fasteners per arm, captive pressnuts and canopy standoff integration as starting topology. Use the upstream separate AIO hardware approach as reference; verify actual hole positions and arm extraction before asserting compatibility. Prefer ordinary hardware over custom guides or raised deck unless measured interference proves unavoidable.

Upstream tree snapshot: https://github.com/OpenRacer/OpenRacer/tree/15477b200a569dad9d4107e77fdb7cac5acfffd9
Reference files:
- cad/Carbon/2mm_BottomPlate_JM_Light.step
- cad/Carbon/2mm_MidPlate_JM_Light.step
- cad/Carbon/Arms/5mm_Arm_JM_Light.step
- cad/Carbon/Arms/5mm_Arm_XV_4_Inch_12x12mm.dxf
- cad/Carbon/2.5mm_BottomPlate.dxf
- cad/Carbon/2.5mm_MidPlate.dxf
- JM_OpenRacer_Light_README.md

The existing 4-inch XV arm is especially useful as a shorter-arm reference. The JM Light provides a 2 mm plate baseline and separate AIO hardware. File inventory and README verified; geometry not yet imported or measured. Do not scale fastener holes, pressnut seats or electronics patterns uniformly. Shorten arm span and revise motor pads; preserve root interface where packaging permits. Target 4 mm arms, 6 mm shaft candidate, 2 mm plates; these are subject to comparison against actual upstream geometry. Keep optional braces out of first prototype unless testing warrants them.

Before importing: retain upstream GPL-3.0 license and notices, record exact commit and file provenance, mark modifications and make corresponding editable sources available as applicable. Use GPL-3.0-compatible distribution; confirm project licensing and name clearance before release. No upstream geometry copied in this PR.

Next: import upstream STEP/DXF into Fusion, measure actual root and plate interface, map all hole centers and arm extraction, then adapt motor position and mount pattern for 116/136 mm wheelbases. Compare plate envelope against prop swept disks before deciding whether to shrink it. Retain upstream architecture by default; document each departure and its reason. R1 is historical exploration only, not a prototype recommendation.
