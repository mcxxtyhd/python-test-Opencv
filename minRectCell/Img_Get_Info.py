import cv2
import xml.etree.ElementTree as ET

from minRectCell.detecMinRect import detect_theminiest_rect
from minRectCell.img_rect import cell_rect

def get_cell_rect(xml_path):

    # 初始化xml处理器
    tree = ET.parse(xml_path)
    root = tree.getroot() #前三句导入数据并获取根元素

    # 获取图片的路径
    img_path=root[2].text

    # 读取图片
    img = cv2.imread(img_path)

    # 读取图片
    img2 = cv2.imread(img_path)

    # 获取所有细胞的  标签 以及  四个点坐标的   集合
    cell_collection=[]

    # 找到所有的对象
    for Obejct_Node in root.findall('object'):

        label_information=Obejct_Node[0].text
        xml_xmin =int(Obejct_Node[4][0].text)   #737
        xml_ymin =int(Obejct_Node[4][1].text)   #265
        xml_xmax =int(Obejct_Node[4][2].text)   #787
        xml_ymax =int(Obejct_Node[4][3].text)   #314

        # cv2.rectangle(img, (xml_xmin, xml_ymin), (xml_xmax, xml_ymax), (255, 0, 0), 1)

        # 这是标注的区域
        label_area = cell_rect(xml_xmin,xml_xmax,xml_ymin,xml_ymax,label_information)

        # 这就是标记的图像   从原图上截下来
        new_img = img[label_area.ymin:label_area.ymax, label_area.xmin:label_area.xmax]

        # 检测图片的最小矩形包围区域   返回新的检测值
        new_rect=detect_theminiest_rect(new_img)

        if new_rect!='ErrorCell':
            # 获得新的坐标
            test_min_x = xml_xmin + new_rect.xmin
            test_max_x = xml_xmin+new_rect.xmax
            test_min_y = xml_ymin+new_rect.ymin
            test_max_y =xml_ymin+new_rect.ymax

            # cv2.rectangle(img2, (new_rect.xmin, new_rect.ymin), (new_rect.xmax, new_rect.ymax), (0, 0, 255), 1)
            # cv2.rectangle(img2, (test_min_x, test_min_y), (test_max_x, test_max_y), (0, 255, 0), 1)

            # 写值
            Obejct_Node[4][0].text = str(test_min_x)
            Obejct_Node[4][1].text = str(test_min_y)
            Obejct_Node[4][2].text = str(test_max_x)
            Obejct_Node[4][3].text = str(test_max_y)

    tree.write(xml_path)
    # cv2.imshow("org", img2)

# xml文件的地址
# xml_file_path = 'cellTwo.xml'

xml_file_path = 'test/test1.xml'
get_cell_rect(xml_file_path)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

