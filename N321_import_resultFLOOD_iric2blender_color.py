import bpy
from bpy.props import FloatVectorProperty, StringProperty
from . import material
from . import N001_lib
import os

# iricの計算結果をblenderのimport
class ImportResult_iRIC2blender_color(bpy.types.Operator):
    #ラベル名の宣言
    bl_idname = "object.import_result_color_iric2blender"
    bl_label = bpy.app.translations.pgettext("3-2-1: import calculation data of Nays2d Flood (Depth / Color)")
    bl_description = bpy.app.translations.pgettext("3-2-1: import calculation data of Nays2d Flood (Depth / Color)")    
    bl_options = {'REGISTER', 'UNDO'}

    # ファイル指定のプロパティを定義する
    filepath: StringProperty(
        name="File Path",      # プロパティ名
        default="",            # デフォルト値
        maxlen=1024,           # 最大文字列長
        subtype='FILE_PATH',   # サブタイプ
        description="",        # 説明文
    )
    filename: StringProperty(
        name="File Name",      # プロパティ名
        default="",            # デフォルト値
        maxlen=1024,           # 最大文字列長
        description="",        # 説明文
    )
    directory: StringProperty(
        name="Directory Path", # プロパティ名
        default="",            # デフォルト値
        maxlen=1024,           # 最大文字列長
        subtype='FILE_PATH',   # サブタイプ
        description="",        # 説明文
    )




    # 実行時イベント(保存先のフォルダの選択)
    def invoke(self, context, event):
        # ファイルエクスプローラーを表示する
        self.report({'INFO'}, "保存先のフォルダを指定してください")
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}


    #実行ファイル（選択しているオブジェクトの地形データをiricの点群csvに書き出し）
    def execute(self, context):

        #### main ####

        # ファイルパスをフォルダパスとファイル名に分割する
        filepath_folder, filepath_name = os.path.split(self.filepath)

        #3d View 範囲の終了設定
        N001_lib.config_viewports()

        #CSVの読み込み設定
        df_col_list = [2, 3, 5, 6, 7] #Nays2d flood: x,y,depth,z,dummy
        usecols     = [0,1,2,3,4,5,6,7,8,9,10,11] #flood
        
        #カラーコンターの設定
        color_set = N001_lib.setting_color_contor()
        mat_list    = []
        mat_list    = material.set_material(mat_list,color_set)
        result_type = "depth"

        ws = N001_lib.Make_WaterSurface_depth_velocity_from_iRIC_result(df_col_list,usecols,filepath_folder,mat_list,color_set,result_type)
        ws.create_mesh_result()

        return {'FINISHED'}
