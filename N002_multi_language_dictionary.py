import bpy



translation_dict = {
    "ja_JP": {
        # system
        ("*", "Add-on for mutual cooperation between iRIC and blender"):
            "iRICとblenderの相互連携用アドオン",
        ("*", "Principled BSDF"):
            "プリンシプルBSDF",
        ("*", "Image Texture"):
            "画像テクスチャ",
        ("*", "Site-package File Path"):
            "site-packageのファイルパス",
        # iric setting
        ("*", "color contour depth setting:"):
            "コンターの水深の設定",
        ("*", "color contour depth setting:"):
            "コンターの流速の設定",
        ("*", "water color setting:"):
            "水の色の設定:",
        ("*", "water surface texture roughness setting:"):
            "水面のテクスチャの粗さの設定:",
        ("*", "water surface texture reflection setting:"):
            "水面のテクスチャの反射の設定:",
        ("*", "water surface texture transparency setting:"):
            "水面のテクスチャの透過の設定:",
        ("*", "image import setting:"):
            "画像読込関係",
        ("*", "download image zoom level setting"):
            "ダウンロード画像のZoomレベルの設定",
        ("*", "download image resolution setting"):
            "ダウンロード画像の解像度の設定",
        ("*", "grid EPSG setting"):
            "格子のEPSGの設定",
        ("*", "image download destination setting"):
            "画像のダウンロード先の設定",
        ("*", "1:google satelite image"):
            "1:google 衛星画像",
        ("*", "3:GSI ortho image"):
            "3:国土地理院オルソ画像",
        # Library
        ("*", "1-1-1: import iRIC grid(csv)"):
            "1-1-1: iRIC格子(csv)の読み込み",
        ("*", "1-1-2: download image from iRIC grid(csv)"):
            "1-1-2: iRIC格子(csv)から画像をダウンロード",
        ("*", "1-2-1: texituring the image to mesh on Blender"):
            "1-2-1: 画像をBlenderの格子に貼付",
        ("*", "1-3-1: import vegetation data from iRIC grid (Nays2dh)"):
            "1-3-1: iRIC格子(Nays2dh/植生データ)を読み込み",
        ("*", "2-1-1: download building data from OSMBuilding"):
            "2-1-1: OSMBuildingから建物データをダウンロード",
        ("*", "2-1-2: import building data from OSMBuilding downloaded data"):
            "2-1-2: OSMBuildingから建物データを読み込み",
        ("*", "2-2-1: import DEM data (obj) from Plateau"):
            "2-2-1: Plateau DEMデータ(obj)を読み込み",
        ("*", "2-2-2: import building data (obj) from Plateau"):
            "2-2-2: Plateau 建物データ(obj)を読み込み",
        ("*", "2-3-1: attach the selected object to mesh surface"):
            "2-3-1: 選択したオブジェクトを接地",
        ("*", "3-1-1: import calculation data of Nays2dh (Depth / Color)"):
            "3-1-1: Nays2dhの計算結果(水深/Color)の読み込み",
        ("*", "3-1-2: import calculation data of Nays2dh (Velocity / Color)"):
            "3-1-2: Nays2dhの計算結果(流速/Color)の読み込み",
        ("*", "3-1-3: import calculation data of Nays2dh (Depth / Water)"):
            "3-1-3: Nays2dhの計算結果(水深/Water)の読み込み",
        ("*", "3-1-4: import calculation data of Nays2dh (Riverbed Variation)"):
            "3-1-4: Nays2dhの計算結果(河床変動)の読み込み",
        ("*", "3-2-1: import calculation data of Nays2d Flood (Depth / Color)"):
            "3-2-1: Nays2d Floodの計算結果(水深/Color)の読み込み",
        ("*", "3-2-2: import calculation data of Nays2d Flood (Velocity / Color)"):
            "3-2-2: Nays2d Floodの計算結果(流速/Color)の読み込み",
        ("*", "3-2-3: import calculation data of Nays2d Flood (Depth / Water)"):
            "3-2-3: Nays2d Floodの計算結果(水深/Water)の読み込み",
        ("*", "4-1: export csv topography data for iRIC"):
            "4-1: 地形データをiRIC用にCSVで書き出し",
        ("*", "4-2: export shp building data from OSMBuilding for iRIC"):
            "4-2: OSMBuildingの建物をshpに書き出し"
     }
}
