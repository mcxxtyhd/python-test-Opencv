import xml.etree.ElementTree as ET

def get_cell_rect(xml_path):

    # 初始化xml处理器
    tree = ET.parse(xml_path)
    root = tree.getroot() #前三句导入数据并获取根元素

    # 找到所有的对象
    for Obejct_Node in root.findall('object'):

        xml_xmin =int(Obejct_Node[4][0].text)   #737
        xml_ymin =int(Obejct_Node[4][1].text)   #265
        xml_xmax =int(Obejct_Node[4][2].text)   #787
        xml_ymax =int(Obejct_Node[4][3].text)   #314

        Obejct_Node[4][0].text="theotest"
        # Obejct_Node[4][0].text = test_min_x
        # Obejct_Node[4][1].text = test_min_y
        # Obejct_Node[4][2].text = test_max_x
        # Obejct_Node[4][3].text = test_max_y

    tree.write('cellThree.xml')


# xml文件的地址
xml_file_path = 'cellOne.xml'

get_cell_rect(xml_file_path)


