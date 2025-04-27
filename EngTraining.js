import React, { useState, useEffect } from 'react';
import { View, Text, TouchableOpacity, StyleSheet, ScrollView, Button } from 'react-native';

const alphabet = 'abcdefghijklmnopqrstuvwxyz'.split('');

const GameScreen = () => {
  const scriptText = "Do you want some milk?";
  const scriptWords = scriptText.split(' ');

  const [currentIndex, setCurrentIndex] = useState(0);
  const [displayedText, setDisplayedText] = useState('');
  const [highlightKeys, setHighlightKeys] = useState([]);
  const [recognizedText, setRecognizedText] = useState('');
  const [accuracy, setAccuracy] = useState(null);
  const [listening, setListening] = useState(false);

  useEffect(() => {
    const firstLetters = scriptWords.map(word => word[0].toLowerCase());
    setHighlightKeys(firstLetters);
  }, []);

  const handleKeyPress = (key) => {
    if (key.toLowerCase() === highlightKeys[currentIndex]) {
      const nextWord = scriptWords[currentIndex];
      setDisplayedText(prev => prev ? `${prev} ${nextWord}` : nextWord);
      setCurrentIndex(prev => prev + 1);
    }
  };

  const startListening = () => {
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    if (!SpeechRecognition) {
      alert('브라우저가 음성 인식을 지원하지 않습니다.');
      return;
    }
  
    const recognition = new SpeechRecognition();
    recognition.lang = 'en-US';
    recognition.interimResults = false;
    recognition.maxAlternatives = 1;
    recognition.continuous = true;  // 추가: 끊기지 않고 듣게 설정
  
    recognition.start();
    setListening(true);
  
    recognition.onresult = (event) => {
      const spokenText = event.results[0][0].transcript;
      console.log('Recognized:', spokenText);
      setRecognizedText(spokenText);
      calculateAccuracy(spokenText, scriptText);
      setListening(false);
      recognition.stop(); // 결과가 나오면 인식 중단
    };
  
    recognition.onerror = (event) => {
      console.error('Speech recognition error', event.error);
      if (event.error === 'no-speech') {
        alert('말소리가 감지되지 않았어요! 버튼을 누르고 바로 말을 시작해보세요.');
      } else {
        alert('음성 인식 오류 발생: ' + event.error);
      }
      setListening(false);
    };
  };
  

  const calculateAccuracy = (spoken, original) => {
    // 소문자로 변환하고, 특수문자 제거
    const normalize = (text) =>
      text.toLowerCase().replace(/[^a-z\s]/g, '').trim();
  
    const spokenWords = normalize(spoken).split(' ');
    const originalWords = normalize(original).split(' ');
  
    let matchedCount = 0;
  
    // 단어 단위 비교
    const minLength = Math.min(spokenWords.length, originalWords.length);
    for (let i = 0; i < minLength; i++) {
      if (spokenWords[i] === originalWords[i]) {
        matchedCount++;
      }
    }
  
    const accuracy = Math.round((matchedCount / originalWords.length) * 100);
    setAccuracy(accuracy);
  };
  

  return (
    <View style={styles.container}>
      {/* 스크립트 영역 */}
      <View style={styles.scriptContainer}>
        <Text style={styles.scriptText}>{displayedText || '스크립트를 맞춰보세요!'}</Text>
      </View>

      {/* 음성 인식 버튼 */}
      <View style={styles.voiceContainer}>
        <Button 
          title={listening ? "🎙️ Listening..." : "🎤 Start Speaking"}
          onPress={startListening}
          color={listening ? 'red' : 'blue'}
        />
        {recognizedText !== '' && (
          <View style={{ marginTop: 10 }}>
            <Text>📝 당신이 말한 것: {recognizedText}</Text>
            <Text>🎯 정확도: {accuracy}%</Text>
          </View>
        )}
      </View>

      {/* 키보드 영역 */}
      <ScrollView contentContainerStyle={styles.keyboardContainer}>
        {alphabet.map((char, index) => (
          <TouchableOpacity
            key={index}
            style={[
              styles.keyButton,
              highlightKeys.includes(char) ? styles.highlightKey : styles.normalKey
            ]}
            onPress={() => handleKeyPress(char)}
          >
            <Text style={styles.keyText}>{char.toUpperCase()}</Text>
          </TouchableOpacity>
        ))}
      </ScrollView>
    </View>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#fff', paddingTop: 50 },
  scriptContainer: { flex: 0.2, justifyContent: 'center', alignItems: 'center' },
  voiceContainer: { flex: 0.2, justifyContent: 'center', alignItems: 'center' },
  scriptText: { fontSize: 24, fontWeight: 'bold', textAlign: 'center' },
  keyboardContainer: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    padding: 10,
    justifyContent: 'center',
  },
  keyButton: {
    width: 40,
    height: 40,
    margin: 5,
    borderRadius: 5,
    justifyContent: 'center',
    alignItems: 'center',
  },
  highlightKey: {
    backgroundColor: 'dodgerblue',
  },
  normalKey: {
    backgroundColor: 'lightgray',
  },
  keyText: { color: 'white', fontSize: 18 },
});

export default GameScreen;
