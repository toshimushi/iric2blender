# iRIC2Blender

## Japanese 

<details>
  
### iRIC2Blenderについて
- iRIC2BlenderはBlender用のアドオンであり、iRICの計算結果をBlenderに読み込み三次元モデル化を行ったり、Blenderで編集を行った地形データをiRICに受け渡すことができます。

#### iRIC
- iRICについては以下を参照ください。
  
  <img src="https://i-ric.org/data/images/common/signature03mono.gif" width="200">
 
  - [iRICホームページ](https://i-ric.org/ja/)
- 現在、Nays2DH,NaysFloodの計算結果の出力に対応してます。
</br>

#### Blender
- Blenderについては以下を参照ください。
  <img src="https://www.blender.org/wp-content/uploads/2020/07/blender_logo_no_socket_white.png" width="200">

  - [Blenderホームページ](https://www.blender.org)

  - Blenderの[編集]->[プリファレンス]->[アドオン]->[インストール]を選択し、`iric2blender.zip`を選択し、アドオンを実装することができます。
</br>

---
### 必須外部ライブラリ
- iRIC2Blenderではpyproj,staticmap,matplotlib等の外部ライブラリ(python)を使用しています。

- Blenderのpythonの場所が不明な場合はBlenderを開いて確認します。[scripting]タブを選択し、[scripting]タブのコンソール画面に以下のコマンドを入力します。

  ```
  >>> import sys
  >>> sys.path
  ```
- Windowsの場合は以下のような出力結果が出てきますので、コマンドプロンプトもしくはPowershellにおいて、以下のフォルダにアクセスし、Pythonを探します。

  ```
  C:\Program Files\Blender Foundation\Blender 3.2\3.2\python\bin\
  ```

- Blenderのpythonが見つかったら、pythonに以下の外部ライブラリを追加してください。

  ```
  > .\python.exe -m pip install --upgrade pip

  > .\python.exe -m pip install pyproj
  > .\python.exe -m pip install requests
  > .\python.exe -m pip install Pillow
  > .\python.exe -m pip install staticmap
  > .\python.exe -m pip install matplotlib
  ```

- 外部ライブラリのインストールが完了したら、以下のコメントを入力し、外部ライブラリが入っているかを確認します。
  ```
  > .\python.exe -m pip list
  ```

- Blenderに戻り、[scripting]タブのコンソール画面で以下のコマンドを入力し、外部ライブラリが無事にインポートできるか確認します。エラー等が生じない場合は無事にインポートできます。

  ```
  >>> import pyproj
  >>> import staticmap
  >>> import matplotlib
  ```

- エラー等が生じる場合(特に初回)、は以下のコマンドで再度外部ライブラリを追加・更新します。

  ```
  >.\python.exe -m pip install --upgrade --force-reinstall matplotlib
  >.\python.exe -m pip install --upgrade --force-reinstall requests
  >.\python.exe -m pip install --upgrade --force-reinstall Pillow
  >.\python.exe -m pip install --upgrade --force-reinstall staticmap
  ```

---
### Blender4.2 外部ライブラリエラー対応
- Blender4.2より、アドオン等の扱いに変更等があったことから、外部ライブラリがblender内のpythonにインストールされているものの、Blenderのコンソールからのパスが通っていないことで、pyprojなどの外部ライブラリの読み込みができないエラーなどが生じる場合があります。
-【参考】pythonの場所が不明な場合はBlenderを開いて確認します。[scripting]タブを選択します。
  ```python
  >>> import sys
  >>> sys.path
  ```
- Blender外のターミナルより、blenderのpythonのパスを確認します。
  ```python
  import sys
  print(sys.executable)
  ```
  - windowsの場合の例
      >"C:\\Users\\XXXXX\\AppData\\Roaming\\Python\\Python311\\site-packages"
  - mac
    > /Users/XXXXX/.local/lib/python3.11/site-packages/pyproj/__init__.py

- Blenderの`[編集]`→`[プリファレンス]`→`[アドオン]`→`[iric2blender]`を選択し、`[site-packageのファイルパス]`欄にファイルパスを追加します。
  - ファイルパスの例(win)：
    >"C:\\Users\\XXXXX\\AppData\\Roaming\\Python\\Python311\\site-packages"
  - ファイルパスの例(mac)：
    >"/Users/XXXXX/.local/lib/python3.11/site-packages"

- `[スクリプト作成]`のコンソール画面より、`import pyproj`など外部ライブラリを呼び出し、エラー等が生じなければ無事にインポートできています。

---
### リリースノート
#### ver.0.1.230228 update by toshimushi
* preview version
  
#### ver.0.2.240908 update by toshimushi
* Blender4.2に対応等
* 多言語化対応（英語／日本語）

---
### License
- iRIC2Blenderは、GPL Licenseを付与しており、営利/非営利目的に関わらず無償で利用することができますが、その正確性や妥当性を保証するものではないことを認識ください。そのため利用にあたっては、利用者責任とします。利用者が何らかの損害を被った場合でも一切負担、責任を負いません。

</details>


---
## English

<details>

### Overview of iRIC2Blender
- iRIC2Blender is the addon for Blender, which allows to make the calculation result on iRIC into 3d model and to generate exportable terrain data from Blender to iRIC. 

#### About iRIC
- Please refer the following url about iRIC.
  <img src="https://i-ric.org/data/images/common/signature03mono.gif" width="200">

  - [iRIC Website](https://i-ric.org/en/)
- iRIC2Blender allows to import the calculation result from Nays2DH and NaysFlood, the popular model on iRIC, into Blender.
</br>

#### Blender
- Please refer the following url about Blender.
  <img src="https://www.blender.org/wp-content/uploads/2020/07/blender_logo_no_socket_white.png" width="200">

  - [Blender Website](https://www.blender.org)
</br>

### Necessary External Library
- iRIC2Blender uses external library such as pyproj, staticmap, matplotlib, etc. 
- Please install the following external library to your python on Blender.


  ```
  > .\python.exe -m pip install pyproj
  > .\python.exe -m pip install requests
  > .\python.exe -m pip install Pillow
  > .\python.exe -m pip install staticmap
  > .\python.exe -m pip install matplotlib
  ```

### Blender 4.2 External Library Error Resolution

- From Blender 4.2, due to changes in how add-ons are handled, external libraries may be installed in Blender's Python environment, but the path may not be recognized from Blender's console. This can lead to errors where external libraries like pyproj cannot be loaded.
- [Reference] If you don't know your Blender's Python location, open Blender to check. Select the [Scripting] tab and enter the following in the console:
    
    ```python
    import sys
    sys.path
    ```
    
- Check the path of your Blender's Python from a terminal outside of Blender.
    
    ```python
    import sys
    print(sys.executable)
    ```
    
    - Example output on Windows
        
        > "C:\\Users\\XXXXX\\AppData\\Roaming\\Python\\Python311\\site-packages"
        > 
    - Example output on Mac
        
        > /Users/XXXXX/.local/lib/python3.11/site-packages/pyproj/init.py
        > 
- In Blender, go to `[Edit]` → `[Preferences]` → `[Add-ons]` → `[iric2blender]`, and add the file path of site-packages to the `[site-package file path]` field.
    - File path example (Win):
        
        > "C:\\Users\\XXXXX\\AppData\\Roaming\\Python\\Python311\\site-packages"
        > 
    - File path example (Mac):
        
        > "/Users/XXXXX/.local/lib/python3.11/site-packages"
        > 
- From the console screen in `[Scripting]`, try importing external libraries like `import pyproj` in the console. If no errors occur, the import was successful.


### Release notes
#### ver.0.1.230228 update by toshimushi
* preview version

#### ver.0.2.240908 update by toshimushi
* Compatibility with Blender 4.2, etc.
* Multilingual support (English/Japanese)


### License
- iRIC2Blender is granted a GPL license and can be used free of charge regardless of whether it is for commercial or non-commercial purposes, but please be aware that it does not guarantee its accuracy or validity. Therefore, users are responsible for their use. Even if the user suffers any damage, we will not bear any burden or responsibility.

</details>