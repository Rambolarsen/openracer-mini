# Retention layout R1 — shared center concept

Exploratory dimensions in mm. Both variants use 4 mm carbon arms, 6 mm shafts and 2 mm plates. This is a dimensioned planar study, not a printable or machinable assembly.

## Common geometry
Local coordinates u along each arm outward from frame center, v transverse. Rotate the same root by 90 degrees for the four positions. Root rectangle u=8..30, v=±5; shaft begins after a radiused transition outside the capture zone. Root is 10 mm wide. Minimum gap between adjacent rectangular roots is sqrt(2)*(8-5)=4.243 mm. Center plate concept: union of a 36 x 36 square and four radial tabs u=8..31, v=±8; use generous fillets at tab transitions. Both plates initially share this envelope, not necessarily hole patterns. Nominal sandwich height 8.2 mm (2+4.2+2); actual spacer height must be matched to measured laminate and clamp behavior. Do not rely on a loose 0.2 mm vertical gap for retention. Battery pad and strap must clear underside screw heads.

## A — guided/keyed root
Use straight, outward-open guide channels formed by fixed spacer/guide pieces between plates, not an undercut that traps the arm. Root width 10, guide clear width 10.3 (0.15 per side nominal). Guides occupy u=12..28, v=±5.15..±7.5. One dedicated M2 clearance hole (2.2 diameter candidate) at u=26, v=0. Positive bearing against guides resists in-plane rotation; bolt prevents radial extraction. Guide mounting and bearing load transfer into plates are unresolved; compare captive spacers and independent guide fasteners before making a solid model. Removing the bolt must not release guide pieces or neighboring arms.

## B — two-bolt control
Same root and plate outline, no guide pieces. M2 clearance holes at u=10 and 26, v=0. Inner hole has only 0.9 mm net ligament to root end (10-8-1.1): reject this inner location for flight prototype. Trial u=12 gives 2.9 mm ligament but reduces clearance to stack hardware to 0.531 mm using assumed radii. Test a staggered or revised root before selecting. Outer hole at u=26 has 2.9 mm net ligament to root end. No strength approval implied.

## Critical stack conflict
The 25.5 square AIO holes project at u=18.031, v=0, inside the solid root. Conventional through-stack screws would pin the arm, defeating independent replacement. Both concepts therefore require an independent electronics mounting interface terminating above the arm layer (e.g. a separate raised mounting deck or captive flush insert in upper plate). Do not drill stack holes through arms. A 2 mm carbon plate alone is not assumed to provide adequate thread engagement. Select real hardware and verify pullout, underside flushness, electrical isolation and Z clearance; until then neither concept satisfies repairability. Outer bolt at u=26 is outside nominal board square along diagonal, but tool/connector access remains unverified; underside access with captive upper hardware is preferred.

## Next coupon
Model one root, plate pair and guide spacers with actual fastener models; print fit-only coupons at guide widths 10.2/10.3/10.4, measure actual clearance, record play and extraction. Test with neighboring root mockups and independent stack mount installed. Then carbon coupon load tests, not flight on printed parts. No manufacturing exports until stack mount and guide load path are resolved.
