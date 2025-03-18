---
aliases: 
source: 
author: 
tags: 
createdAt: 2025-03-17T11:21:00
categories: 
status: false
---

1. 使用内存存储替代 localStorage
2. 在本地环境中运行项目

让我们先修改代码以使用内存存储，然后我会给您在 VSCode 中本地运行的指令。


```tsx
import React, { useState, useEffect, useRef, useCallback } from 'react';
import { Volume2, Settings, Upload, Eye, EyeOff, Play, Pause, RotateCcw, Palette } from 'lucide-react';
import { Button } from '@/components/ui/button';
import { Slider } from '@/components/ui/slider';
import { Input } from '@/components/ui/input';
import { Switch } from '@/components/ui/switch';
import { Tooltip, TooltipContent, TooltipProvider, TooltipTrigger } from '@/components/ui/tooltip';
import { Popover, PopoverTrigger, PopoverContent } from '@/components/ui/popover';
import { Label } from '@/components/ui/label';

// Word type definition
type Word = {
  word: string;
  phonetic: string;
  meaning: string;
  lastReviewed?: number;
  reviewCount?: number;
};

// In-memory storage
const memoryStorage = {
  data: {} as Record<string, string>,
  setItem(key: string, value: string) {
    this.data[key] = value;
  },
  getItem(key: string) {
    return this.data[key];
  }
};

const DanmakuVocabulary: React.FC = () => {
  const [words, setWords] = useState<Word[]>([]);
  const [speed, setSpeed] = useState(5);
  const [showPhonetic, setShowPhonetic] = useState(false);
  const [showMeaning, setShowMeaning] = useState(false);
  const [isPlaying, setIsPlaying] = useState(true);
  const [fontSize, setFontSize] = useState(16);
  const [danmakuColor, setDanmakuColor] = useState('#FFFFFF');
  const [backgroundColor, setBackgroundColor] = useState('#1F2937');
  const containerRef = useRef<HTMLDivElement>(null);
  const fileInputRef = useRef<HTMLInputElement>(null);

  // Load saved settings from memory storage
  useEffect(() => {
    const savedSettings = memoryStorage.getItem('danmakuSettings');
    if (savedSettings) {
      const parsedSettings = JSON.parse(savedSettings);
      setSpeed(parsedSettings.speed || 5);
      setShowPhonetic(parsedSettings.showPhonetic || false);
      setShowMeaning(parsedSettings.showMeaning || false);
      setFontSize(parsedSettings.fontSize || 16);
      setDanmakuColor(parsedSettings.danmakuColor || '#FFFFFF');
      setBackgroundColor(parsedSettings.backgroundColor || '#1F2937');
    }
  }, []);

  // Save settings to memory storage
  useEffect(() => {
    const settings = {
      speed,
      showPhonetic,
      showMeaning,
      fontSize,
      danmakuColor,
      backgroundColor,
    };
    memoryStorage.setItem('danmakuSettings', JSON.stringify(settings));
  }, [speed, showPhonetic, showMeaning, fontSize, danmakuColor, backgroundColor]);

  // Handle file upload
  const handleFileUpload = useCallback((event: React.ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files?.[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = (e: ProgressEvent<FileReader>) => {
        const content = e.target?.result as string;
        const lines = content.split('\n').filter(line => line.trim() !== '');
        const newWords = lines.slice(1).map(line => {
          const [, word, phonetic, meaning] = line.split(',').map(part => part.trim());
          return { word, phonetic, meaning, lastReviewed: Date.now(), reviewCount: 0 };
        }).filter(word => word.word && word.phonetic && word.meaning);
        setWords(newWords);
        memoryStorage.setItem('words', JSON.stringify(newWords));
      };
      reader.readAsText(file);
    }
  }, []);

  // Load words from memory storage
  useEffect(() => {
    const savedWords = memoryStorage.getItem('words');
    if (savedWords) {
      setWords(JSON.parse(savedWords));
    }
  }, []);

  // Create single danmaku
  const createDanmaku = useCallback((container: HTMLDivElement, wordObj: Word) => {
    const danmaku = document.createElement('div');
    let displayText = wordObj.word;
    if (showPhonetic) displayText += ` ${wordObj.phonetic}`;
    if (showMeaning) displayText += ` ${wordObj.meaning}`;
    
    danmaku.textContent = displayText;
    Object.assign(danmaku.style, {
      position: 'absolute',
      color: danmakuColor,
      fontSize: `${fontSize}px`,
      textShadow: '2px 2px 4px rgba(0,0,0,0.5)',
      transition: 'right linear',
      whiteSpace: 'nowrap',
      cursor: 'pointer',
      right: '-200px',
      //很可能是这里,-30 可能远远不够 .这样会由于显示过高而看不到.
      top: `${Math.random() * (container.offsetHeight - 30)}px`, 
    });

    container.appendChild(danmaku);
    danmaku.offsetHeight; // Force reflow (不知道为什么VS会警告)

    danmaku.style.right = `${container.offsetWidth + 200}px`;
    danmaku.style.transitionDuration = `${15 / speed}s`;

    danmaku.addEventListener('transitionend', () => {
      container.removeChild(danmaku);
    });

    danmaku.addEventListener('click', () => {
      alert(`${wordObj.word}\n${wordObj.phonetic}\n${wordObj.meaning}`);
      if ('speechSynthesis' in window) {
        const utterance = new SpeechSynthesisUtterance(wordObj.word);
        utterance.lang = 'en-US';
        speechSynthesis.speak(utterance);
      }
      // Update review information
      const updatedWords = words.map(w => 
        w.word === wordObj.word 
          ? { ...w, lastReviewed: Date.now(), reviewCount: (w.reviewCount || 0) + 1 }
          : w
      );
      setWords(updatedWords);
      memoryStorage.setItem('words', JSON.stringify(updatedWords));
    });
  }, [showPhonetic, showMeaning, speed, fontSize, danmakuColor, words]);

  // Other functions remain the same...

  // Render component remains the same...
};

export default DanmakuVocabulary;

```

这个更新版本的组件使用了内存存储来替代 localStorage，这样应该可以解决您遇到的 DOMException 错误。

现在，让我给您在 VSCode 中本地运行这个 React 项目的步骤：

1. 确保您的系统已安装 Node.js 和 npm。

2. 在 VSCode 中打开一个新的终端（Terminal -> New Terminal）。

3. 创建一个新的 React 项目（如果您还没有的话）：
   ```
   npx create-react-app danmaku-vocabulary --template typescript
   cd danmaku-vocabulary
   ```

4. 安装必要的依赖：
   ```
   npm install lucide-react @radix-ui/react-slider @radix-ui/react-switch @radix-ui/react-tooltip @radix-ui/react-popover
   ```

5. 将更新后的 `DanmakuVocabulary` 组件代码复制到 `src/components/DanmakuVocabulary.tsx` 文件中。

6. 在 `src/App.tsx` 中导入并使用这个组件：
   ```tsx
   import React from 'react';
   import DanmakuVocabulary from './components/DanmakuVocabulary';

   function App() {
     return (
       <div className="App">
         <DanmakuVocabulary />
       </div>
     );
   }

   export default App;
   ```

7. 运行开发服务器：
   ```
   npm start
   ```

8. 在浏览器中打开 `http://localhost:3000` 查看运行结果。

如果您在运行过程中遇到任何问题，请告诉我，我会帮您解决。同时，请注意，由于我们使用了 shadcn/ui 组件，您可能需要额外的设置步骤来正确导入这些组件。如果您遇到相关的导入错误，请让我知道，我会提供更详细的设置说明。