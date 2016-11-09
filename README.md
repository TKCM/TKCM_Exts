# MultiChannelWeightMap
I customized basic WeightMap to multi channel weight map.  
And added some mouse events. example brushStrength, brushBlur, brushTypeSelection, and map value drawing with box object.  
Please check video for details. <https://vimeo.com/190755793>  
At the moment, the biggest problem is to can not Undo & Redo painting actions.  
  
標準で提供されているウェイトマップがシングルチャンネルだったため、マルチチャンネル対応へ拡張を行いました。  
更にブラシの強さ、ブラシのボケ足、ブラシタイプ（エアーブラシ、スタンプ、バケツ）の変更をマウスイベントに追加しました。  
またマップの濃さを視認しやすくすることを目的としたボックス表示の機能もマウスイベントに含めました。  
詳しくは上記リンクの映像をご覧ください  
現在の大きな問題としてUndo/Redoには対応できていません。