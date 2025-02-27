# Cyber Shooter - Time Attack 🚀
 --- 

 
# วัตถุประสงค์ของโครงการ (Objective)

พัฒนาเกมยิง 2D แนว Arcade ผสม Time Attack ที่ท้าทายความเร็วและความแม่นยำของผู้เล่น โดยผู้เล่นจะควบคุมยานอวกาศที่ต้องยิงและทำลายอุกกาบาตที่ตกลงมา พร้อมกับอัพเกรดความสามารถของตัวเองเพื่อให้สามารถเอาชนะความท้าทายในแต่ละระดับได้มากยิ่งขึ้น
----


# ขอบเขตของงาน (Scope of Work)

พัฒนาเกมโดยใช้ภาษา Python ใน VS Code
สร้างระบบการควบคุมตัวละคร (เคลื่อนที่และยิงกระสุน)
สร้างระบบศัตรูที่เป็นอุกกาบาต (meteorites) ที่มีพลังชีวิต (HP)
พัฒนาระบบจับเวลาให้ผู้เล่นต้องทำลายอุกกาบาตก่อนเวลาหมด
เพิ่มระบบอัปเกรดให้ผู้เล่นสามารถเลือกพัฒนาความสามารถของตัวละครในแต่ละระดับ

ผู้ใช้งาน (Player)

	•	เล่นเกม ยิงเป้าหมาย เก็บคะแนนในเวลาจำกัด

	•	ใช้ Power-ups หรือไอเทมเสริม (ถ้ามี)

	•	ดูคะแนนและอันดับใน Leaderboard

ผู้ดูแลระบบ (Admin)

	•	ปรับแต่งค่าต่าง ๆ เช่น เวลา, ความเร็ว, อัตราการเกิด Power-ups

	•	จัดการข้อมูลคะแนนสูงสุดและฐานข้อมูลผู้เล่น (ถ้ามี)

	•	ตรวจสอบข้อผิดพลาดของเกมและอัปเดตเวอร์ชัน


----


# ระยะเวลาโครงการ (Project Duration)

⏳ เริ่มต้น 1 มกราคม 2568

🎯 สิ้นสุด 31 มีนาคม 2568

----


# งบประมาณ (Budget)

💰 ค่าใช้จ่ายในการพัฒนา (ฟรี) หากใช้เครื่องมือและทรัพยากรที่ไม่มีค่าใช้จ่าย
ค่าใช้จ่ายเพิ่มเติมอาจมีในส่วนของกราฟิก เสียง หรือเครื่องมือเสริม (ถ้ามี)

---


# ผู้รับผิดชอบโครงการ (Stakeholders)

👤 นาย พัชรพงษ์ ดีมงคล  465415241007

---



# ผลลัพธ์ที่คาดหวัง (Expected Outcomes)

🎯 เกม 2D Sci-Fi Shooter ที่สามารถเล่นได้จริง พร้อมระบบยิงและจับเวลา

🎯 ผู้เล่นได้รับประสบการณ์ที่สนุก ท้าทาย และพัฒนาทักษะการเล่น

🎯 เกมสามารถเผยแพร่หรือพัฒนาเพิ่มเติมในอนาคต

----


# ข้อกำหนดทางเทคนิค (Technical Requirements)

🔹 พัฒนาโดยใช้ภาษา: Python 🐍

🔹 ใช้ไลบรารี: Pygame หรือไลบรารีอื่น ๆ ในการพัฒนาเกม

🔹 รองรับแพลตฟอร์ม: PC (Windows, Mac, Linux)

🔹 เครื่องมือพัฒนา: Visual Studio Code 🖥️


----
----


# ฟังก์ชันที่ใช้ในโปรแกรม

🔹 get_player_name(): รับชื่อผู้เล่นจากการป้อนข้อมูลผ่านคีย์บอร์ด

🔹spawn_boxes(): สร้างอุกกาบาตที่ผู้เล่นต้องยิงทำลาย

🔹 upgrade_menu(): แสดงเมนูให้ผู้เล่นเลือกอัพเกรดในแต่ละระดับ

🔹 load_leaderboard() และ save_leaderboard(): โหลดและบันทึกคะแนนสูงสุดในไฟล์ JSON

🔹 display_leaderboard(): แสดงตารางอันดับของผู้เล่น



----

🎮  # วิธีเล่น


🔹 ควบคุมตัวละคร
ใช้ ลูกศรซ้าย (←) / ขวา (→) เพื่อเคลื่อนที่
กด Spacebar เพื่อยิงกระสุน


🔹 เป้าหมายของเกม
ยิง ทำลายบล็อกศัตรู ที่ปรากฏในแต่ละด่าน
บล็อกแต่ละอันมี พลังชีวิต (HP) หากถูกยิงจน HP หมด บล็อกจะถูกทำลาย


🔹 ระบบเวลา
ผู้เล่นต้อง ทำลายบล็อก ก่อนเวลาหมด ⏳
หากเวลาหมดก่อนที่จะทำลายบล็อกทั้งหมด = Game Over ❌


🔹 ระบบอัปเกรด
เมื่อผ่านด่าน จะมี เมนูอัปเกรด ให้เลือก 1 อย่าง จาก 3 ตัวเลือก:

1️⃣ เพิ่มความเร็วตัวละคร

2️⃣ เพิ่มความเร็วกระสุน

3️⃣ เพิ่มพลังทำลายของกระสุน



🚀 ฟีเจอร์เด่นของเกม


✅ ความท้าทาย ⏳ - ด่านจะยากขึ้นเมื่อเลเวลเพิ่มขึ้น!

✅ ระบบเลเวล & อัปเกรด 🆙 - ยิ่งเล่น ยิ่งเทพ!



💥 เป้าหมายหลัก
พยายามไปให้ไกลที่สุด ทำลายบล็อกให้ไว และ อัปเกรดให้เหมาะสม เพื่อเอาตัวรอด! คุณจะไปได้กี่ด่าน? 🔥
---
ขน
