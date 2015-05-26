# Phatch - Photo Batch Processor
# Copyright (C) 2007-2008 www.stani.be
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see http://www.gnu.org/licenses/
#
# Phatch recommends SPE (http://pythonide.stani.be) for editing python.

# Embedded icon is taken from www.openclipart.org (public domain)

# Follows PEP8

from core import models
from lib.reverse_translation import _t
from lib.imtools import convert_safe_mode


def init():
    #lazily import
    global Image
    import Image
    global generate_layer
    from lib.imtools import generate_layer


def watermark(image, mark, horizontal_offset=None, vertical_offset=None,
        horizontal_justification=None, vertical_justification=None,
        orientation=None, method=None, opacity=100):
    """Adds a watermark to an image."""
    if image.mode == 'P':
        image = convert_safe_mode(image)
    layer = generate_layer(image.size, mark, method,
        horizontal_offset, vertical_offset,
        horizontal_justification, vertical_justification,
        orientation, opacity)
    return Image.composite(layer, image, layer)


class Action(models.StampMixin, models.Action):
    """Apply a watermark with tiling, scaling and opacity"""

    label = _t('Watermark')
    author = 'Stani'
    email = 'spe.stani.be@gmail.com'
    init = staticmethod(init)
    pil = staticmethod(watermark)
    version = '0.1'
    tags = [_t('default'), _t('filter')]
    __doc__ = _t('Apply with tiling, scaling and opacity')

    icon = \
'x\xda\x01\x95\nj\xf5\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x000\x00\
\x00\x000\x08\x06\x00\x00\x00W\x02\xf9\x87\x00\x00\x00\x04sBIT\x08\x08\x08\
\x08|\x08d\x88\x00\x00\nLIDATh\x81\xd5\x98[L\\\xc7\x19\xc7\x7fsv\xcf\xee\xd9\
\xb3\xbb`p\x80\xf8\x02\xacq\x02\xb5\xe36\xb1\xad\xa4)(VmZ)i\xdaD\xceC\x926\
\xedK\x13\xa5\xae\x1f\xaa\xbeTj\x9f\xda\xa7F\xeaC\x1b\xc5Ul\xc9\x97\x07G\x89\
\xda\xe2T\xc4v\xdc<\x94\xd8\xa2\x89\x8d\x12n\xbep\xf1\x05X\xc0W.\xe1\xba\xf7\
=g\xfap\xf6,\x0b,\x04\xbc[Y\x1d\xe9\x08\x16fg\xfe\xbfo\xfe\xdf73GH)\xf9\x7fn\
\xca\x83\x16\x90ks\xe6{\xc0\x1e!v\x99\xf0\x9a\x84Z\x01\xeb\x01\x1d\xb8)\xe1\
\x9a\x02\x1f\xe8\xf0a@\xcah\xbe\xe6\x13\xf9\xb2P\x9b\x10\xaa\x06o\x0bE\xd9_T\
[\x8b\xfe\xc8#\xb8\xcb\xcap\xf8|\xc4GG\x89\x8f\x8c0\xd1\xd2B$\x18\xec2\xe0G\
\xdf\x92r \x1f\xf3\xe6\x05\xe0\x8a\x10e\x02>\\\xf3\xdcsukw\xee\xc4]T\x04B\
\xa4f\x10\x19\xb3\t\xa6;:\xb8s\xe2\xc4\xb8\x0c\x85^\xda"es\xaes\xe7\x05\xa0K\
\x88\x7fm8x\xf0\xd95\xfb\xf6!\xef\xde%y\xecXjtK|\x1a!\xf59\xd2\xdf\xcf\xf0\
\xb1cQ\x0c\xa3f\xab\x94C\xb9\xcc\x9ds\x12_\x11\xe2y\xe0Y\x7f}\xbd\xa5q\xedZ\
\x8cD\x82d$B2\x1c&\x19\x0e\x93\x88DHF\xa3$#\x11\x8cH\x04\xd7\xbau\x14\xd5\
\xd5i&\xfc1\xd7\xf9sNb\x01\xbfW\x8b\x8b\x89\x7f\xfc1\xea\x9e=$/_&1=\r\x80\\\
\xb0\x02"\xe3\xb3VQ\x81\x80\x9ft\x0b\xf1\xd6V)\xbb\xeew\xfe\x9c\x00\xda\x84\
\xd05\xd8\xae\x16\x15\x11\xef\xed%\xd6\xdb\x8b\x04\xa4\xa5\x16\x84\xc06\xa8\
\x10"\r\xa2\x08\x81\xe2\xf5\x02\x08\x13\xbe\x07<\x18\x00\x17<\x0c8\xe3\xa3\
\xa3$B!K\xbc\x10\xd6\x03\xf3\xc4\x83\x15y\x1b$16\x86\t(\xb0-\x17\r9\x01|\x13\
\x82\xdd\x10\x89MO{\xa2##(^/\xa6\x10\x98X \x82\xb9\xd5\xb0\x85\x0bK4\xb3\xfd\
\xfd\x18\x80\x03\x86\x1f\x18\x00R\x9aR\x88n\x13v\x8e\xb5\xb4P\xf8\xd4SH\x87#\
\r\x90\xaeoBX\xd5"\xf53\xf1\xd5WL\xf5\xf4\xe0\x04\x04\xf4>8\x00\xc0\x80OL\
\xd8\x99\x98\x9ef\xb4\xb5\x15\xef\xe6\xcd\xa0ii+\xa5\x9b\x108\x80\xd8\xd8\
\x18\xe1\xeb\xd7\x11R\xa2\x80\x11\x86\x96\\\xe6\xcfy\x1f\xb8$\xc4\xa6\x18\
\xdcH\x82\x12\x07\x92B\xe0\\\xbb\x16\xa7\xcf\x87\xa2i\x08U\xc5\x88\xc50\xa3Q\
\x12\xe3\xe3\x98\xa1\x10N\xac\xc8\xa9\xf0\xc9\xb7\xa5|\xee\x81\x02\x00|)\xc4\
\xa7Q\xd8\x9d\x00\x0c \x99z\xcc\x8c>J\xeaqf<.x\xf1;R\x9e\xcce\xee\xbc\x9cF\
\x93p\xd4\xc4\x12l2\'\xde\x00\x12\xcc\x01%S\x7f3\x01QRbh_|1\x99\xeb\xdcy\x01\
\xb8\x0c\xff\x00\xeeH\xe6\x04&\xb1\xc4/\\\x11\xfb\xff\xae\x97^r\x98\x8a\xf2i\
kk\xeb\x1f\x1a\x1a\x1a\x1c\xf7;w\xdeN\xa3\xe7\x84\xf8m\x0c\xde\x8a3\x17u#\
\xf5d\xdaG\x05\xdc~?%g\xce\x80\xc7c\x7f\xfd?\xa6i\xbe\xf6\xe4\x93O\xae\xba\
\xa4\xe6\xf3B\xf3\xb6\x84q;\xcav\xe43\x7f\xda\xd1\xd7\xf7\xee\xcd\x14\x0f\
\xf0\x8c\xa2(\x17\xdb\xdb\xdb\xf7\xaev\xd2\xbc\x01|W\xca\xa8c\xfb\xf6\x0b\
\xb6\xc8L\xebd\x8a\x17^/\xfa\x1bod\x1b\xa2HJ\xf9\xcf\xb6\xb6\xb6\x83\x17.\\\
\xf0d\xeb\x90\xad\xe5\x05\xe0\xd4\xa9SzCC\xc3\x07\xb7\xdf|\xf3\x87x<H\xe6\
\x12\xda`>@\xe1\x0b/ t}\xb9\xe1\xf6\xb9\\\xae/[[[Wt\xc4\xc8\x19\xa0\xa5\xa5e\
\x8b\xdb\xedn\x05~\x9cTU&_~\x19\x1cVNfZ\t\xc0SQA\xc1\xfe\xfd+\x19\xf61!\xc4\
\x17mmm\xfb\xbe\xaecN\x00\xed\xed\xed?UU\xf5K\x8f\xc7\xb3E\xd34\\.\x17\xa1\
\x9d;\x19~\xf5U\xa2~?BQ0\x00\xa7\xcb\x85RS\xc3CG\x8f.\xf4\xfer\xcd\x03\x1clo\
oo\x1c\x19\x19\t,\xd5\xe9\xbe\x8e\x12\x17.\\\xf0\xb8\\\xae\x03\xc0\xeb\x00\
\xba\xae#\xa5$\x99L\x92L&\tm\xdbF3P\xec\xf7\xb3\xce\xe5"\xb9i\x13%%%\xa8\xd6\
\x11z\xc9&\x84\xc0\xe1p\xe0p8p:\x9d\xb8\xddn\xca\xca\xca^\xbcv\xed\xda\x96\
\xd2\xd2\xd2\x9a\xbc\x00tttl\xf5z\xbd\x1f*\x8a\xf2\r)%RJL\xd3\xc4\xe7\xf3\
\xe1HYgjj\n\x9f\xcf\xc7\xfa\xcaJ*++\xf1\xfb\xfd\xcb\nu:\x9d\xa8\xaa\x8a\xc3\
\xe1H\x1f\xbd5MC\xd7uN\x9f>MWW\xd7\xc4\x13O<\x91U\xcf\xaa\x00\xba\xba\xba\
\xf6\xf9\xfd\xfe\xbf\x08!4[\xb8i\x9a$\x93I\x12\x89\x04\x9a\xa6\xb1~\xfdz\xa2\
\xd1(7n\xdc\xb0\x8e\xd0\xf6]@\x08\\.\x17\x05\x05\x058\x9dN\x1c\x0e\x07\x8a\
\xa2\xa0(J\xba\x9f\xdd\xd7\xeb\xf5\x12\x8b\xc58t\xe8\x10\xd3\xd6\xedN\x08!\
\x84\xcc\xb2i\xad\x08\xa0\xad\xadM/..n(..\xfe\x01\x80i\x9a\xc4b1\xe2\xf18\
\xf1x\x1c\xc30\xe6\x06t:y\xf4\xd1G\x19\x1a\x1aBQ\x94\xf4\xaa\xe8\xba\x8e\xae\
\xeb\xb8\xdd\xeey\xe23\x01\x14EA\xd7uzzz\xf8\xe8\xa3\x8f\xd2cJ)\x05\xe0\x10B\
\x18\x0b!\xbe\x16\xa0\xaf\xaf\xef\xa9\xf2\xf2\xf2\xd3\xaa\xaa\x96\x84\xc3afg\
g\x89D"\xf3D/lB\x08\xea\xeb\xeb\x99\x98\x98\xc0\xe1p\xa0\xeb:\x85\x85\x85\
\xf8\xfd\xfe\xb4ul\x08[\xbcm\xa5S\xa7N\xd1\xd55\xff\x86)\xa5T\xb06q)\x8403!\
\x96\x05\xe8\xeb\xeb\xfb\x93\xdb\xed\xfe\xf5\xe4\xe4\xa4:;;\xcbj\x8e\x1dB\
\x08\x8a\x8b\x8b\xf1\xf9|\xd8\x15j\xa1x\x1b\xc0\xe1p\x10\x0e\x879|\xf80SSS\
\x8b\xc62MS\x01\\XU9\xf3\xb6\xba4\xc0\x91#G6\xed\xd9\xb3\xe77B\x08fffV,<\xb3\
9\x9d\xcetr\xdb\xbe\xcf\xb6\x02\xdd\xdd\xdd466f\x1d#\x14\n1<<\x9c:}\x13\x07\
\x8c\xcc|X\x12\xe0\xd6\xad[\x89\xf7\xde{\x8f\xba\xba:\xb6o\xdf\xce\xad[\xb7H\
$\x12\xab\x02\xd0u=m\r\x1b 3\x81\r\xc3\xe0\xe4\xc9\x93\\\xb9r%\xeb\xf7\xef\
\xdd\xbb\xc7\x9d;wZ\xcf\x9e=\xfb\x0b\xac=K,\xec\x93u#\x13B\x88P(\xa4\x02|\
\xfe\xf9\xe7\x9c8q\x82u\xeb\xd6QXX\xb8*\x00\x9f\xcf\x87\xaa\xaa\xf3 \x9cN\'B\
\x08\xa6\xa6\xa6x\xf7\xddw\xb3\x8a7\x0c\x83\xbe\xbe\xbeDOO\xcf\xdf\x1b\x1b\
\x1b\x7f755\x15a\x81u\x96\x04\x10V-Sfgg]\xf6\xdf\xee\xde\xbd\xcb\xa1C\x87\
\x88\xc7\xe3l\xd8\xb0!]\xee\x96k\x0b}oW$)%\xdd\xdd\xdd\x1c8p \xab\xdf\xc3\
\xe10\xdd\xdd\xdd\xd3\xe7\xcf\x9f\xff\xf3\xb9s\xe7\xfe\x06L\x03\x11,\xfb\x98\
\x80\xfc\xba$\x16\x80#\x12\x89\xcc\xdb\xf3M\xd3\xa4\xa1\xa1\x81\xc7\x1f\x7f\
\x9c]\xbbvq\xfb\xf6mb\xb1\xd8\x92\x00>\x9foQ\x894M\x93\xd3\xa7O/i\x99\x91\
\x91\x11\x82\xc1`_SS\xd3\x81X,6\x04\xdc\x03&\x80P\n\xc0N\xe2t\x9b\x07`G\x1fP\
gff\xfcR\xcaE\xd1\xbex\xf1"\xc1`\x90W^y\x85X,\xc6\xf8\xf8\xf8\xe2\x08\x08\
\x81\xd7\xebM\x7f\xd7\xae2\xc7\x8f\x1fgrr\xf1-\xd20\x0c\x06\x06\x06\x92\xc1`\
\xb0\xe9\xb3\xcf>kH\t\x1f\x01\xc6\xb1V \x8cuO2W\xb2\x0f\x08\xc0944$5M\x9b\
\x0e\x04\x02\x05\xaa\xaa\xce\xeb\x10\x0e\x87y\xff\xfd\xf7\xa9\xaf\xaf\xa7\
\xb2\xb2\x92\x9b7o\xce\xdb\x17t]OG^\xd34z{{ill\xccZ\x86\xc3\xe10\xfd\xfd\xfd\
3\x9d\x9d\x9dGo\xdc\xb8\xd1\x96\x12?\x8a\x15\xf9Y,\xfb$\x00CJi.\xfc\xfe\xbc+\
\xa5\x10\xc2\xbe\xf9\xe9@q \x10xl\xc7\x8e\x1d\xef\x94\x97\x97\x07\x8a\x8a\
\x8a\xd2\xfd4M\xc3\xedv\xe3v\xbb\t\x04\x02<\xfd\xf4\xd3\xdc\xbbw\x8fP(\x04@I\
I\t\x85\x85\x85\xb8\xddn\xce\x9c9\xc3\xe5\xcb\x97\xb3\xc4)m\x99\xfe\xa6\xa6\
\xa6wb\xb1\xd8\xadT\xd4\xc7\x80),\xdb\xc42"\xbfH|6\x00\x91\x02\xf0\x00k\x802\
`c}}\xfd\xaf***v\x95\x97\x97+\x8a\xa2\xe0v\xbb\xf1x<h\x9a\x86\xa6ix\xbd^jkk\
\x91R266FUU\x15\x89D\x82\xe3\xc7\x8fgMT\xc30\x08\x06\x83\xc9\xc1\xc1\xc1\xa6\
\xe6\xe6\xe6\x13\xc0\xddT\xd4\xbfb\xce2qR\xef\x02\xb2\x9d\x81\x96\x03p`m\x1a\
>`m\nb\xfd\x96-[\x9e\xd9\xb6m\xdb\xcf\xaa\xaa\xaa\xbc>\x9f/}\xb6\xf1x<i\x98@\
 @MM\rW\xaf^]\xd62}}}3\x9d\x9d\x9dG\xfb\xfa\xfal\xcb\x8caYf\x06\x88\x92\x91\
\xb0\xcb\x89_\x04\x90\x82\xb0m\xa4\xa5 \x8a\x80\x12\xe0a\xaf\xd7[\xb1{\xf7\
\xee_VTT\x046n\xdc\x88\xd7\xeb\xc5\xe3\xf1\xa4at]\'\x1a\x8d\xd2\xd9\xd9\x99u\
\xb2\x91\x91\x11\x06\x07\x07\x07\xce\x9d;w \x14\n\r3\x97\xa8\x93\xac\xd02+\
\x01\xb0+\x91\x13p\x03^\xa0\x10k5J\x81\xb2\xda\xda\xda\xbdUUU\xbbkjj\xd4\x82\
\x82\x82y\xab\x11\x89D\xb8~\xfd\xfa\xbc1M\xd3$\x18\x0c&\x83\xc1\xe0\xa7\xcd\
\xcd\xcd\r\xe4`\x99\x85mQ\x15\x92RJ!\x84\xfdn\xca\xbe\x9f\xdb/\xd9b@\xf4\xfc\
\xf9\xf3\x1f\x0c\x0f\x0f_\t\x87\xc3?\xaf\xae\xae^SVV\x86a\x18$\x12\t\xe2\xf1\
\xf8\xbc\xf1\xc2\xe10\x03\x03\x03\xb3\x1d\x1d\x1dG2\xaa\xcc}[fa[\xf2\xc5Vj%\
\xec\x9cP\x99\xb3T!\xf0\x10P\xaa\xaa\xea\xfa\xfa\xfa\xfa\xd7+++\xb7n\xde\xbc\
Yh\x9a\x86\x94\x92\x89\x89\t\x00FGG\x19\x1c\x1c\x1c8{\xf6\xec_C\xa1\xd0\x10y\
\xb0\xcc\x8a\x012@2_\xac\xb9\xb1Jl\x01P\x8c\x95\x1be;v\xec\xf8~uu\xf5\x0b\
\xd5\xd5\xd5n\x8f\xc7C8\x1cfpp0\x19\x0c\x06\xcf677\xff\x83<Zf\xd5\x00)\x08;/\
\xec\n\xa5\x01~\xac\x04\x7f\x08()--\xddTWW\xb7\xbf\xac\xacl\xdd\xf8\xf8\xf8\
\xf4\xa5K\x97\x0e_\xbdz\xb5=%|\x14+\xea9[\xe6\xbe\x002 lK\xd9U\xcaN\xf0"\xac\
}\xc3\xb7{\xf7\xee\xe7[[[\xff=333\x8e\xe5\xf3\tV\xb11\xfd\xcf\x00\x16\x80dZ\
\xca\x93\x02\xf1\xa5~wbY#\x82u\x14\xb0\x8f\x03y\xb1\xcc"=\xf73V\x06\x84}Wu\
\xa7\x1e\x15k\x852\xab\x96\x1d\xf5\xbcXfa\xfb/\xb0\xe2\xc5j\xcb\x8b\xb4\xe9\
\x00\x00\x00\x00IEND\xaeB`\x82O\xe6\x0f\xa5'
