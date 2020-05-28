# fraudml

running manufacture.py or manufacture2.py creates input.csv or input2.csv respectively.

input.csv contains only amount to fraud mapping
input2.csv contains amount and count to fraud mapping

txnamt_feature.py - is not working. Maybe because of running it with high epoch. should reduce the epochs to 150 and try again

amt_cnt_feature.py - is somewhat working. When ran with epochs=1500, accuraccy was 72%
  when ran with epochs=250, accuracy was 92%
  whan ran with epochs=150, accuracy was 98%
  
debugs are saved in .txt files.
