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
</br>

### 必須外部ライブラリ
- iRIC2Blenderではpyproj,staticmap,matplotlib等の外部ライブラリ(python)を使用しています。
- Blenderのpythonに以下の外部ライブラリを追加してください。

```
> .\python.exe -m pip install pyproj
> .\python.exe -m pip install requests
> .\python.exe -m pip install Pillow
> .\python.exe -m pip install staticmap
> .\python.exe -m pip install matplotlib
```
  
  
### リリースノート
#### ver.0.1.230228 update by toshimushi
* preview version
  

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

### Release notes
#### ver.0.1.230228 update by toshimushi
* preview version

### License
- iRIC2Blender is granted a GPL license and can be used free of charge regardless of whether it is for commercial or non-commercial purposes, but please be aware that it does not guarantee its accuracy or validity. Therefore, users are responsible for their use. Even if the user suffers any damage, we will not bear any burden or responsibility.

</details>