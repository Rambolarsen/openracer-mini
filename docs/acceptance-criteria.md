# Proposed engineering acceptance criteria
Status: draft for review; numbers are engineering proposals, not proven limits.

| Criterion | Mini 3 | Mini 3.5 |
|---|---|---|
| Frame mass incl canopy/hardware (provisional planning target, not a release gate) | 20 g | 30 g |
| Ready-to-fly mass incl battery | <=120 g | <=180 g |
| Nominal wheelbase | 116 mm | 136 mm |
| Static adjacent prop tip gap | >=4 mm | >=4 mm |
| Mechanical arm swap | <=5 min | <=5 min |

Define frame mass excluding electronics, motors, props and battery. Time arm swap from safe disconnected state, excluding motor transfer and electrical reconnection; record total repair time separately. No electronics removal allowed. Validate actual swept envelope including flex and tolerances, not only nominal static gap. True-X spacing = wheelbase/sqrt(2); nominal gaps 5.82 and 7.27 mm. Require no prop contact with canopy, cables or battery throughout tested envelope.

Before flight: fit check real components; verify electrical isolation, fastener engagement, motor screw lengths, secure battery, cable and antenna retention, and access to configuration ports. Use restrained instrumented motor/prop testing with suitable guards; require current below manufacturer limits with documented margin, voltage and temperature within component limits, no resets or video dropout. Initial AIO15 screening target <=12 A per motor steady state (80% of rating), bursts below published limit. Actual race duty and all-motor thermal tests required. Establish mechanical test loads from measured baseline and expected use; no arbitrary structural certification. Compare arm root and center plate damage after repeatable load tests; retire cracked parts. Record all results by revision; printed fit checks are not flight articles.

Open decisions: exact motor/prop pair, structural load cases, temperature limits, camera tilt range, battery selection and licensing. Do not close physical verification tasks on documentation alone.
