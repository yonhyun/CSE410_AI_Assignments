q1=infer.query(['Flu'],evidence={'Fatigue':0})['Flu']
q2=infer.query(['Flu'],evidence={'Fatigue':0,'FluShot':1})['Flu']
q3=infer.query(['Flu'],evidence={'Fatigue':0,'FluShot':0})['Flu']
q4=infer.query(['Flu'],evidence={'FluShot':0,'Fever':0,'FluShot':1})['Flu']
q5=infer.query(['Lyme'],evidence={'Fatigue':0,'FluShot':1})['Lyme']
q6=infer.query(['Lyme'],evidence={'Fatigue':0,'FluShot':0})['Lyme']