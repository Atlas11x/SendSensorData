const int LED_BLUE = 6;
const int LED_WHITE = 4;
const int FOTORESISTOR_MAIN = A0;

int Massive_data_foto_main[20];

//?? function
int GetSizeArray(){
  return sizeof(Massive_data_foto_main)/sizeof(Massive_data_foto_main[0]);
}

int data_foto_main = 0;

void InitPin(){
  //Led for start-stop recive data
  pinMode(LED_BLUE, OUTPUT);

  //Led for indicate process Get data from sensor (write array)
  pinMode(LED_WHITE, OUTPUT);

  //Pin for getting data from fotoresistor
  pinMode(FOTORESISTOR_MAIN, INPUT);
}

void setup() {
  InitPin();
  Serial.begin(9600);

  //??init array
  for(int i = 0; i < GetSizeArray(); ++i){
    Massive_data_foto_main[i] = 0;
  }
}

void loop() {
  data_foto_main = analogRead(A0);
  Serial.println(data_foto_main);
  delay(500);
  //?? led indicate of start receive data
  digitalWrite(LED_BLUE, HIGH);
  //??process getting data and put it in array
  for(int i = 0; i < GetSizeArray(); ++i){
    Massive_data_foto_main[i] = analogRead(FOTORESISTOR_MAIN);
}
  //?? led indicate of stop receive data
  digitalWrite(LED_BLUE, LOW);
  //?? Serial.println all data in massive to user interface. One time.
  for(int i = 0; i < GetSizeArray(); ++i){
    Serial.println(Massive_data_foto_main[i]);
}
  Serial.println(999);
  //?? stop receive data
  while (true){
  }
}
