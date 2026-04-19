#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x3F, 16, 2);

void setup() {
  Serial.begin(115200);
  lcd.init();
  lcd.backlight();
  lcd.setCursor(0, 0);
  lcd.print("Waiting for data");
}

void loop() {
  if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\n');
    Serial.println("Received: " + data);
    
    if (data.startsWith("T:")) {
      lcd.setCursor(0, 0);
      lcd.print("T:" + data.substring(2) + "   ");
    }
    else if (data.startsWith("S:")) {
      lcd.setCursor(0, 1);
      lcd.print("S:" + data.substring(2) + "   ");
    }
  }
}