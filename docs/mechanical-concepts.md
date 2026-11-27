# Mechanical concepts — revision 0
Addresses #4 and #5; exploratory, not a release. Mini 3 first. No upstream CAD copied.

## Coordinate system and skeleton
Origin at frame center; +Y forward, +Z up. Motor centers at (+/-a,+/-a), a=wheelbase/(2 sqrt(2)). AIO holes at (+/-12.75,+/-12.75). Prop disks radius D/2. Mini 3 a=41.012 mm, Mini 3.5 a=48.083 mm. Adjacent motor spacing 82.024/96.167 mm; nominal tip gap 5.824/7.267 mm. AIO mounting holes lie at radial distance 18.031 mm on the arm centerlines. This is the main packaging conflict.

## Retention candidates
A: keyed root with an outward-accessible dedicated bolt and positive tangential bearing faces. Root slides radially outward; captive upper plate remains installed. Design pocket with rounded internal corners, adequate bearing length and a separate load path into both plates. Key clearance, bolt location and plate support remain open.
B: two radial M2 bolts per arm, at r=10 and r=24 for both variants. Nominal screw head radius 2 mm and stack keepout radius 3.5 mm give closest projected gap 0.469 mm for both variants. This is not enough evidence of assembly access: screw head/tool/nut envelopes, component height, tolerance and actual board outline must be checked. The inner bolt sits under the board; use underside access and captive threaded hardware, or reject layout if removal requires lifting the board. Outer bolt lies near the board edge. Both bolts require carbon edge-distance and root strength validation. A shared structural screw must not be needed to remove another arm.
C: one-piece base as mass and stiffness reference only; fails replaceability.

Prefer A for weight exploration, B as simpler mechanical control. Do not select a winner until fit and load tests. Keep electronics isolated from carbon and hardware. Battery removal is permitted during repair.

## Mass budget (comparative, not CAD measured)
Start both variants with 8 mm wide, 3 mm thick arms, common root geometry and 1.5 mm plates. Do not assume 4 mm arms are needed on Mini 3.5; assess stiffness, motor loads and crash durability first. Wheelbase increases from 116 to 136 mm, so radial arm length increases 10 mm. With assumed carbon density 1.55 g/cm3, four straight 8 x 3 mm extensions add 4 x 10 x 8 x 3 x 1.55 / 1000 = 1.488 g. This excludes changes in motor pad area, taper and holes. Use net profile area x thickness x density / 1000 for actual CAD mass. Shared plates and hardware would add no differential mass; larger electronics canopy and motor pads may add some. Do not publish absolute predicted frame mass until profiles and hardware are defined. Existing 20/30 g frame targets remain ceilings, not predictions; aim for similar structural mass. Include all canopy, straps, pads and frame hardware in measured frame mass. A longer cantilever can increase bending and torsion even with identical cross section; compare both variants experimentally and increase thickness only if justified.

## Fusion 360 implementation
Create user parameters from cad/shared/parameters.csv (units in column; variant columns are values, not direct Fusion import format). Sketch construction diagonals and motor centers; constrain AIO hole pattern independently; add prop disk construction circles and board footprint; add separate retention keepouts; project only reference geometry into arm and plate components. Keep one master arm rotated in four occurrences. Create independent components for upper/lower plates, electronics and battery; measure real component Z envelopes before setting standoff heights. No DXF export yet.

## Validation plan
1. Print non-flight root/plate coupons for both retention concepts; test assembly with real hardware and a board mockup, then actual unpowered board.
2. Verify single-arm extraction with other arms and electronics installed, tool access and cable routing. Record mechanical swap time and total repair time.
3. Measure play before/after repeated assembly; establish load cases from actual motor thrust and representative crash loading; compare carbon coupons in controlled bending/torsion with documented loads, inspect root and plate damage.
4. Replace placeholder areas and weights with measured data; review before full carbon order.

No Fusion native CAD, measured hardware envelope or structural validation exists yet. The Python skeleton is a reproducible planar reference, not a solid model.
