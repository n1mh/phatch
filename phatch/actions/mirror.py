# -*- coding: utf-8 -*-
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
# Phatch recommends SPE (http://pythonide.stani.be) for editing python files.

# Embedded icon is designed by Arielle B Cruz (http://www.abcruz.com/)

#Follows PEP8

from core import models
from lib.reverse_translation import _t
from lib.imtools import convert_safe_mode, paste

#---PIL


def init():
    global Image
    import Image

# Declare constants here

BOTH = _t('Both')
HORIZONTAL = _t('Horizontal')
VERTICAL = _t('Vertical')

DIRECTIONS = [BOTH, HORIZONTAL, VERTICAL]


def tile(image, direction):
    if image.mode == 'P':
        image = convert_safe_mode(image)
    result = Image.new(image.mode, get_dimensions(image, direction))
    paste(result, image, (0, 0))

    if direction == BOTH:
        x_mirror(image, result)
        y_mirror(image, result)
        xy_mirror(image, result)
    if direction == HORIZONTAL:
        x_mirror(image, result)
    if direction == VERTICAL:
        y_mirror(image, result)

    return result


def get_dimensions(image, direction):
    width, height = image.size
    x_scale, y_scale = get_scales(direction)
    return width * x_scale, height * y_scale


def get_scales(direction):
    x_scale, y_scale = 1, 1

    if direction == BOTH:
        x_scale, y_scale = 2, 2
    if direction == HORIZONTAL:
        x_scale = 2
    if direction == VERTICAL:
        y_scale = 2

    return x_scale, y_scale


def x_mirror(image, result):
    width, height = image.size
    paste(result, image.transpose(Image.FLIP_LEFT_RIGHT), (width, 0))


def y_mirror(image, result):
    width, height = image.size
    paste(result, image.transpose(Image.FLIP_TOP_BOTTOM), (0, height))


def xy_mirror(image, result):
    paste(result, image.transpose(Image.ROTATE_180), image.size)

#---Phatch


class Action(models.Action):
    label = _t('Mirror')
    author = 'Juho Vepsäläinen'
    email = 'bebraw@gmail.com'
    init = staticmethod(init)
    pil = staticmethod(tile)
    version = '0.1'
    tags = [_t('transform'), _t('filter')]
    __doc__ = _t('Symmetrical tile texture')

    def interface(self, fields):
        fields[_t('Direction')] = self.ChoiceField(DIRECTIONS[0],
                                    DIRECTIONS)

    # TODO
    icon = \
'x\xda\x01\xcb\x0e4\xf1\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x000\x00\
\x00\x000\x08\x06\x00\x00\x00W\x02\xf9\x87\x00\x00\x00\x04sBIT\x08\x08\x08\
\x08|\x08d\x88\x00\x00\x0e\x82IDATh\x81\xad\x9a\xc9\x8f\x1d\xc9q\xc6\x7f\x91\
\x99\xf5\xb6\xde\xb8\r\xd9\xe4P\x14-Yc\x8d\x04k\xa3\x96\x815:\xe8\xe0\xb3\
\xe5\x83}\xf0\xd5:\x1a\xf0\xd50\xe0\x93\x05\xfd\x15\xfa\x0f|\x92\x8e\x06|\
\xb2\x84\x81F\xcbh\x19\x18cY\x965\xa4\xb85\x87C\xb2\x97\xb7TUF\xf8\x10Y\xcb\
\xeb\x19@:\xa8\x81\xea\xaa\xf7^\xd5\xeb/2\xe2\x8b\xf8"\xb2\xe5{\xdf\xfc\xda?\
\x00\xdf\x0eU\xda\x93\x18\xf9\xa3\xfc\x98\xa1M\x8b\xa9\x02 !\x10\xaa\x04"\
\x7f\x9c\xaf\xcf\x19m\xda\xa5\x99\xfds\x02\xbe}\xfb\x93\xd5\xde\xcb;w- B\x08\
 \x11$A\x88\xe5:\xfa5\xdd{\x01B\xda\xfeL"\xd2\xdf\x9fX\xeb\x84_\xfc\xf0\x11f\
\xc6g\xber\x9dy\xac\xc12X\x8bi\xf6\xeb\xeel\x19\xb4\x05\xd3s\xaf\xc7\xf7\x95\
\xd7\xaa(f\x0f\x96\xb7\x16\xff\xf7N\xf3\xad\x14g\xd3\xbd[\xbb\xbf\xb1\xb9>\
\x17B\xe5 %B\xa8\x10I\x05h\x82\x98@Z\x08Uy\x0f\x08@\x10DB\x7fM\x08\x10\x02{\
\x01\x0e?z\t3\xe3\xa5=0\r\xa0\n*`@6\xcc\xd4\xc1i\xeb\x00\xb5\x1d\xaeexm\xa1\
\x05m\xdc\x00iA\x1b\xb9\xb5\x9b\xed\xde\xecc\xbbIR$\xc6(\x84\xdd\xb2\xea\t\t\
~\xb6\x90z#\xac3\xa4\xfb\xfc\xfc\xbd2\xbe\x8eXL\xc4\x89b\x06\x96\x16X\xceH(\
\x80\xb4EB\x8bh\xf1\x866\xc53\x83\x01\xa2\x19\xac\xf1{;Cl06\x92DR$\x01\x10g\
\x10&H\xa8@\xa2\x03/\xe0\xad\x80\x92qH\x85\xe4\xf7\xf6FF\xa4\x181\x18\x18!\
\xac\xc1\x0c\xd2\x0e\x12s\x01\x98\x11k@3fcp-\x92;O\xf8gt\xe0\x8bqR\xc2\xca\
\xb4\x01\x0b\xe0\xf1\xe2\x06H\x15\xca*V#0]\\\'\x90\xca\xaf\xcbk\xeb\x81VX\
\xcf\x81\xb1g\x02\xc8\x0b\x04C\xd2\xc2\r)a`:\x00\xed\xc1Y\x0b\xb1\x80\xcd\
\x19\xb1\xc1\x03nt1L[_\x80\xb6\x1d\x0c\x908\x85j\x0e!~p\x15e\xb8\xb6\x98F\
\xbc\x88C\x88uD\x0e\xe3\xcf\xc5\xc9\x8e\xf9w\x9bx\xc8X\xe3\xe1\xd1\x81\xefb\
\xbf\x84\x87Y\x8b\x84\xb1a\xf9\\x\xf9}b\xab\x91\x07\xd2\x0c\xaa\xdd\x0248Q\
\xbb\x15-1\xdd\x85N\xc7\x05\x19\x87\xd3y\xa3B,\x06D7 -<\xfdi\xee\xc3\xa0\x07\
\xab\xe3\xccTV96e\xd5\xcb}\xbd\x07\xc6\x99\xc9\xc6!4E&;%TF)\xb4\x80\x1abzt.\
\xb1O\x88\x18\x1d\x81c\xefE\x01\xbf\xcf\x0c\xd2\x1cC\xb6\xd2c\xbf\xba=\x17\
\xbaT\xd9\x0e\x99\xa9\xbc\'\x9a\x81\xee\xfdr_S\x03\xcd`\x00\xd5\xeev8\x9c\
\x0b\x8d\xad\xf7\xfbs!\xb0$,DL\xc6\x9c\xb1\xde\x03\x92\x16P\x0c\xe8\x80\x87\
\x0f\x03\xdf\x81\x0e\xa3Z\xd0\xafzgP\xf6l\x14\x97\xdb\x06H\xda\xd9\x02`\x05\
\xf0@\xcc\xa1\xa8\x85B\xf4\r\xc6\xda\x8c\x14\x12\x8bj^\x9e\x0b\x1eb\xa2\xfeL\
\xf1\x80\x10\xc0Z\x82)X\xcb\xaa]\xd1\x981\x93)\xd3(\x98\xb6h\x97\xebG\xc5\
\xab+z}6\xb2\xec\x06\xc7)p:J\xa3i\xe1\xd9\xa7\xcb(\xa3\x15\x1fW\xd8\x10\x13\
\'\xb9\xe5\xfe\xfa\x05\xcf\xda\rKm\xa9\xc2\x84\xbdj\xc1\x8d\x9d\xcb\\\x9d].F\
\xe0\x86\xa3\x85\x03B@9Z\xbd\xcf\x83\xe5{\x9c4glr\xcd"$.\xa6)/O\xf7\xd8\x9f\
\xec\xa2\xb9a\\\xb1\xa5\x18\xd4q\xa4\x0b;\xd2|;\x8dR\xed`\xa1\x00\xefV_\x12\
\x84\xe0\x9e\x91H\x08\x13\x8e\x9a%o\x9f\x1eqo\xfd\x82\xda\x94 \x11\x10t\xf5\
\x9ck\xcd\x92O\xee\x0b\x1f\xdf\xbf\x89\x84\x8e\xc4\xc1\x93\x04\x81_\x1f\xdf\
\xe3\x9d\x17wy\xb8~F0\x03\x0c\xb5\xccD\x84\x9b\xf5\x92O\xef]\xe3\xb0\xdaA\
\xb5\xf1\xd0*\x95\xba_\xf5\xce\x03\x96!L\xb7I\xec\x1ep\x9d\xd3\xa7\xcd\xde\
\x13\x81\x10*\x8es\xc3\xdbg\xef\xf3\xee\xfa\x84\x14&\xcc%x\xd6\x12\xd7\x15\
\xcf\xda\x9a\xb7^\xdccoq\x85\xc3\xf9\xc5\x12B\nq\xc6\x93\xcd\x0b~\xfa\xe2.\
\xabv\xc3\xbc*u\xc1\x14\xcc02\xf7\xea3\xf4\xec)\xf3\x83\x05\x07\xd5\x82\xdc\
\x93}\xdb\x0b\xdd5\xe9\x9c\x012Y\x00n\x80\x85\x80\x88\x13\xb43BC\xe4\xfe\xfa\
\x98G\xed\x92i5/\x9e\x12\'g1$\x12h\x80_\x1e\xff\x8ek\xbb\xd7<$U\x918\xe5\xed\
\xe3\xfb\xd4\x04&i\xeeae6\x9cM\x89Ay\xd2n\xb8[/\xf9\xf4\xf4\x00\x91<\xaa\t\
\xc5\x0b\xbd\xd8S$\xce\x00\x19\n\x995kd\xb2\xef\x84\x0b\x1d\x19\x9d\xd4"\x91\
\x8d)\xc7\xaa\x10*\xaa8\x19\x80w\xe7\x10\x80\x80\xa8r\xef\xf4\x88\xb3\xdc\
\x96\xfa!,\xb5\xe5\xdd\xd3\xc7,\xd2\x9c\x18"\xd0\xe5q-^P\xc0hr\xc3\x89)\x1bI\
\xcc\xaa\xe96\x89\x0b\xf9iWX\xb3\x8489\x17B\xed\xdasu\xae!\xcd\\\xeb\xc4\t\
\x88 \x92X\xb65\xcf\xeb3\x1am\xc9f\x18\x82\x01jF6CMi\xac\xa5Ue\x9d\x1b\x8e\
\xd6\xc7\xbdG\x9f\xacOx\xef\xec)\xd3\x98H!PI"H J H\xe1;\xfe\x1d/\x9a%g\xed\
\x86\xf9d\x81\x99z\xf6\xc95\xa65\xb4k\xc8\x1b\xc8\xab\x92\x85\xc6$N\x15\x86\
\x14\xe24C\xf7\xa0\nQ!o8[?\xe7\xf1\xc9#bLNN\t\x98\x08F\xa0\xac\'\x10hL\x99M\
\x0f\xd8\x944:\x9d\x1eP[F[\x05\x94\xe27\xd7I#\x0f\xe4\xdc0\xdf\xbd\n{k\xc8\
\xd1\xc1v\xb5\xa0\xf4\x0b&\x82\xc4\t\xe8X\xcc\xa5\xa9\xc7T\x9fy\xb6\xe5\xb3\
\x85\xc4\xa2\xdae\x9e\x16\xacr\xc3\xb4\'\xae}\x80\x07H !\\\xda\xb9\xc6\x0b\
\xf1p\xb9\xbcs\x8d\x14g}\xc8h\x0f\xba\xe3\x80\xf3`\xa3\r\xb38cg\xb2\x87I\xc0\
\x82\xf5^\x94\x12\xd2}e\xd6\x1a\xc4\xdb\x10\x17si\x86\xc49\x96f\xce\x838\xf7\
\\\x1b\xe7X\x9a3\x9b\x1ep\xfb\xe0\x16\x17\xe6\x97\xd0\x90\x90X\xf9!^\xd4\xa4\
H\xec\xc6\x8c;\x87\x9fg\x12\'.\'\x10R\xa8\xf8\xd2\xf5;4f\xbd\xdau\xb9^\xf5\
\xdfc!r0\xbb\xc8\xed\x83\x8f2\x9f]\xe8qt\xb8H\x8e\xa3\xbb\x96\xf3Y\x888\xef\
\x85\x99\x15]#\x92 V\xbd\'>q\xf9\x15\x1e\xd6K\xde8\xfa%Z\xe2\xb8_y\x02\xb5\
\xb6\x1c\xee\\\xe5\xb5\xeb_$J\xc4J\x14\x8a\x08\xaf]\xff"\xbf}q\x97\x07g\x8f\
\x99\x84"5,{\xffLF\xc5x\xf5\xd2+|\xea\xa5WK\x86\x8a\xa5\x01\x1aIji!tz\xc9\
\x86,\xd4Y\xba%\xa5C,=\xc0\xd0q\xc5\x90\xf8\xdaG\xbe\xca\xc1\xce!\xdf\x7f\
\xf8\x13^\xd4\xa7D\x11\xcc\x14\xb5\xcc\x9d\xab\x9f\xe1\xf5\x9b\xaf\xb17\xd9-\
\xc0\xe9\x8dXTs\xfe\xe6\xcf\xfe\x8a\x1f\xdc\x7f\x93\x1f?~\x0b\x11A\x10\xb2e\
\xf6\xaa\x1d\xbez\xfd\x0b|\xee\xf2+D\xa4H\xee\xd2\xe8H\xda\xea\xe4\xd0\x16\
\xa1E:5\xaa\xeb\r\xabM\xcdl\xef\xa5"\xcc\xaa\xd2\xffv\xear\xf0\x00\xa1\xa2\
\x92\xc8\x17^\xfe\x12\xaf^\xfb,O\x96\xefq\xb4z\xcan\xb5\xc3\xf5\xddk\xecV;\
\xa4P&\x1b\xa9\xe2\xf4\xe8\xbe7\'\xb1\x02m\xd9\x9f\xed\xf3\x97\x7f\xf2u\xfe\
\xe2\xe6\x97yxz\xc4Is\xcaK\xf3K\\]\\a\x96\xa6\xae\x93\xb4\xf4\xbf}k9\xea\x93\
s\x91\xe0\x96Y\x9d\x9c\xa0\xeb\r\xf2\xbdo~\xcdvn\x1c\xf2\xf2g?O\xaaf\x9eJ\
\xc7\x15\xb6H\x85q\xa8\x8c\x7f\xcc\x0c97.\x11\x11\x9e?\xf8\r\x8f~\xfc\x06\
\x98qx\xe75.\xdc\xfcS\xcc\xec\xf7>;\xd4\x86su\xa2\x1c\x82\xd1\xb6\x1b\x1e\
\xfc\xe2g\x9c\xfe\xee\x81\x87\x90\xa9bf\xa3?`\x0c\xce\xd7\x02Z\xc7\x10?\x08d\
\xfc\x1a+\x05\xc83\x8cj\xf6\t\xc46\xfe\xee\xe1\xad\'\xc1>\xc4\x00\xeb\x0f\
\xffn\xebgN)\xa4\xc8\xe7\xbe\xf1\xd7\\\xbar\xb3\xc8\xe9.\\\x864:\x0e\xa1NVor\
\xcb\x93\xe5S\x9e\xac\xdec\xa7\xda\xe1\xc6\xee5\x16\xd5\xc2\x89\rH\xacx\xb3\
\xf9WL3_\xfa\xbb\x7fr\x83\x005e\xd5\xaexp\xfa\x98\x93\xfa\x94\x97\xe6\x97\
\xb9\xba\xb8\xc24V\xa3ff\x08\xa1\xf3#\x97.\x84\xae}\xec6o|\xe7;\xa40\x9b\xb2\
\x98M\xb1v\x89\x11\xb1\xe8\xf3 \tqk\xac\xe2\\h\xc8"\xbc\xfd\xfe\xff\xf2\x9f\
\x0f\x7f\xc2\xf3\xfa\x84(\xa9\xac\x9br\xe7\xea\xe7x\xfd\xe6W\xd8\xadv@3{\x87\
\x1fq\xef\x16o,\xdb\x15?\xb8\xffC\xde|\xf4\x16NaP\xcb\xecU\x0b^\xbf~\x87\xcf\
^\xfe\x04\xd1\xac\x00nFm\xa7K\n+<\x80\x96\xf9lJ\x98MK\x16j\xd7\xd0\x96\xb4\
\xa9-\x16\x13\xa6\xa9\xf4\x07\t4!!\xa3\x12\xf8\xfe\xe3\x9f\xf3\xc6\xe3_ \x12\
\x99v\x03.\xbc\xc8\xfc\xf4\xe8\xe7<\\>\xe2o_\xf9\x06\xbb\xd3\xbd\xad\xe8X\
\xb7k\xfe\xedW\xdf\xe5\xfe\xc9CO\xa3]\x88 \xac\xea\x13\xfe\xfd\xb7\xff\xc1\
\xb3\xb3\x87|\xfd\xfa\x1d\x82)fM\xbf\xea\xda\xb7\x96\xcd0\xcdk\xbd\xa9w\x7f\
\xe7Ncl0\xdd \xd9\x0f\xcb5\xd6\xfa\xfb\xa2\r\xbf~\xf6k\xfe\xeb\xe9;x\x17l\
\x04S?P\x82\x19\xd3P\xf1\xf8\xec\x88\x1f=~\x8bl\xb9\xe7\x85\x99\xf1\xa3\xc7o\
\xf1\xf0\xf41\xd30!\x18\xe5\x19?\x12\x101\xdey\xff\x7fx\xe7\xe9\xaf|l\xd2\
\xfd\xfd\\#\xbaA\xf2\x1a+\x18\xd1\x82\x17s\x03,\xd7\xbd`\x92\xee:\xd7n\x88\
\xfa\xb1\xa9\x8f\xb9w\xf2;\x8e7\xc7T\xe5\x0f\xf6\x87)\x11?f!\xf1\xd3G?\xa3\
\xe9\xf5\x94\x91-\xf3\x93G?c\x16"\x91\xec\x87\xe9\xd6wT\x08g\xf5)\xf7N\xee\
\xb1\xde\x1c#\xb9F\xf2\xba,\xe4\x06\xb2c3-\xf8\xda\x8d\x93\xb8\xf3\x80\xe9\
\xc4uw\xa8\x00\xf5\x9e\xd62XB\xcc8k\xd7\x9c\xd6\xa7T".\xdd\xac\xcbT:\x8cO\
\xcaO\xd6\x96\xe7\xcb\xf7J\xe61\x9e-\x9f\xa0\xda\x90$\xf4F\xf9i\xe8\x07@I"\
\x9c5g\x9c\xd6\xc7\xcc\xd2\xbcL\xe0\\\xfb\xd8hZ\xe1\\\xd8\xf8\xc4\xc69\xe0\
\x16ZH\x80!\x96\xb0\xd0\x01\xf3t\x95\xdb\x159o\xf0&\xd1\\\n|X\xaa5\x88\x02\
\xeb\xcd\xf3\x92A\x8c\xf5\xe69\xb1\x84\x9c\xdfk\xa3s\xf9.sO\xe4\\\x93\x9b\
\x95W\x7f\xadG\xc3\xac\xd1\xb8\xd1Z\x0f\xfb\xb1\x07\xb0\x1d/\xcff\x0e\xde\
\x12\x04/\x1c\x861\x0f\x81\xfd4EL\xe9w\x11\xa4\x03^V\xd5\x1c\x8ca\\\x9e,X\
\xe2\xd9\xe7\xf2dA\xea\x0c\xb7\xb1\xe1\x14\xf0\x1dW\x94\xbdT\xb1\x08\xb1\x80\
\x1ft\xd00\xf0-\x06m\x1b\xb0\xf1\xb4%\n\xc1\xbc\x07\x08\n\x9a\xb0\xd2\xac\
\xccC\xe2J5g\x1a\xca\xac\x07\x17S\x03x\xefL\xb2)7\xe6\x97X \x88y\x01[ \xdc\
\x98_\xe2\xd1\xf2=7\xde\xba_\xc3a\x18\x93\x10\xb9R-X\x04A\xf3f\x98\xd6\x8d\
\xf7\x0b\xba!W\xae\x87,d]\xe3`-\x96\x1bD]L\xf9\xb9\x01m\x08\xdap{~\x81[\xf3\
\x8b\x98y\xd6\x89f\xc4\x8e\xd0b@f\x1e#_\xb9\xf2\n\xa1[=k1\xdd\xf0\xda\xe5WX\
\xc4\x04d\xa2t\xe4\x85h\x10\xcc\xf7\n^\x9e\x1d\xf0\xb1\xf9Eb\xd1C\xdb8\x1c\
\x1b%\xbdZ^\x036\xf2@\'Q\xc5\x8aT5D\xcc=b\x8ae\xe3b\x9c\xf0\xf9\xfd\xebD\xe0\
\xfe\xe6\x84\xc6r\t\xa0\x80b\\\x99\xee\xf3\xc9\x83[\xdc\x98\x1dx\xc3\xd1\xc9\
\x89\\s8\xdb\xe7\xcb\x97>\xce\x7f\x1f\xdf\xe5h\xfd\xc2\xc7*\xe6c\x95$\xc2\
\xed\xd9E>\xb3w\xc8\xe54Es\x8d0\x8e\xfds;6\x96\x9d\xb7\xdb!\xd4B0\xc4\x0c\
\x0b=\xaf<#a \xa0\xd9\xb8>\xd9a\xe7\xc2-\xde]\x1f\xf3,oXkf\x12*\x16i\xc6\xcd\
\x9d\xab\xdcX\\\xf1\t\x1b\x83\xde\'o@\x02\x9f\xda\xbb\xce\xa58\xe1\xde\xf2\
\x88\xb3vE\x9d\x1bf!r!N\xb85\xdb\xe7B\x01\xbf\xb5\x15\xa5\x19\x18\xcd\x86\
\xe8\xc6\x8c\xe7\xd2\xa8?P\x04\xa8\tV\xbc!\x1a\x8bB\x05\tF\xce\xca~\xac\xf8\
\xf3\xbd\xabl\xccX\x9b\x92\xc2\x84\x9d\xe4\xe3y\xcd\xb5\x0f\xc8\xbayf1\xc0BB\
5s8\xdd\xe5\xb0\x9a\xb1lW4Z3\x93\xc0T\x04\xb4%\xe7\xday\xd3\xef\xa1\x95]\x19\
\xd3a\xcc\xde\r\xb6\xceg!W\x94\x19\x10\xd7\x1f%\xd78\xdf\\\xb7\xb8Q\xd1\x13\
\xab\x19\x95\xc4\xd2]IYu\xf5Q\xcah3\x03\xb5\xbe\x7f5\xcbh\t\x8b\xb9\x08\xf3\
\x90@3:\xda\xf0\xe8\x00o\x03\xd7~R\'\x961\x8aW\x07\x03j\xa8\x8f\xb1\xd9%\x8f\
}\xeb2\x83\xba\xe4\xb2\xd6\x1f\xb2\x88\x84Rw\x82O\x15L\r\x13C\x82y\x16E@\r\
\xabO\x07\x0e\xd4\xa7\xc8t\xdfS\xb4\xf9\xac_5\xfb\x82u\xd3f\xf5\xc2i%L\xc4\
\xb2/\x88Y\x01\xee\x99\n\t\xb0yv\xde\x805\xf6\xecW0\xd9C&\xfbX\xb5\xe7\x93\
\x8a4\xf7\xd9\x90U>]\x1e\xe6!\xbe*\x9e\xc2<\x99\xb6\x9dA]\xffZ\xba+\x03\xdb<\
\x83\xcd\xf3\xa1]E\xb6\xdaM\x8f]\xeb\xdfGKu\xd6\xc6\xe5C\xbbv\xc1\xd9\x9c`\
\xf5\t\xd4\xc7\x903\x10\xc6jt\x83\xd5\xc7\x10\x9f\xfa\xdc1L\xb00\x818\xdan\
\xed\x8faZ\xdd\xcdP\t\xc1\x8d\x94\x80I\xf06\xb2#qs\x86i\x83\x98b\xa6\x18\xda\
\xaf\xf8\xd61\x9e\x01u\x92A\x1b\x8f\x10\xad\x8bbX\xfb\xe72\x05\x16\xa5#\xcb\
\x1b`\r\x96|\x05\xf3\xbaod\xe4\x03\xfbf\xa3\xb9Q\xff\xba\x1am\x84\x94}d\xf2\
\xa0u\xf2\x1a\xc9]]\xe8\xce\xd9\xb5}\xc9\xebC\xef[v!\xfb\x1a2\xde\xfc\x18\
\xfad\x13\x1b\x0cp\x12\xaf\x86\xadSK\x88\xc6\xfe\x1a\xa9JU-\x1b\xcd\x96\x10\
\xab\x9ct\xa1\xec_\x99\xf7\x10\x84\x16\xb1\xaa\x90\xb0\xf5V\xb5]\x8d\xa6\n\
\xcd\xb9\x1d\xc7n\xe2\xd00T\xdb\xb6/\x82\xd2\x1b\x9d\x87I\x856\xbd\x82\x19\
\xa5\xd1\xb5?\xd4ua\xa3\xa6\x86\xd0\xba!Z<\xa1\xc9w\xcf\xcb\xf5\xd6\xbd\xe53\
\x89M\xcf\x01\xf2\xca\xa7\x13\xa3\rm)\xfb\xc2N\xe0f\x142\xa3\x8d\xeeR\xcde\
\xd4\x95\xa1\x9d\xd7\\\xc6$k3\x9a\xb3\x89.\xc5BU\x00D\'\xee(\xf6\xc7\xe1\xe3\
\x9bw\x1d\xd8\x84\xd8\x00\x9e\xee5\x89\\\xb7\xae\x98\x8a\x07\xba=0\xe9\xe4\
\xc0xd\xa2\xe7F(\xdd\x0c\xc8\x06\xcf1\xea\xcc4Vfm\x96\x94\xd7\x9b\xe5\xdd\
\xb3\xdb\x8b\x97\x17\xefZ0\x11\xcf\x93\t\xac\x10\xd5\xa2\x03+\xaa\xc7\x81\
\x87\x81\xcc\xda\x8d_\xbai\xbb!\xa2\xac\x0c\x1e\xdf}\x1f3\xb8v\xfd\x90y\x18\
\xa6\x0b>\xcb\x15\xb0P\xbe\x9f\xa2\xae\xc3\xe8\xbd\xd4W\xe4\x9e\xe4\x94\x01o\
0\xbb\x7fvK\xdau\xbd\x94\xef\xfe\xfd\xeb\xff(A\xbe\x15\xab\xb8\xfb\x87\xff\
\xbb\xcd\xef\xf9\xb7\x193\xb4\xc9h\xf6ID\x88\x7f\xe8\xbf\xdb|\xd8\xdc\xe5C\
\xee\xca\x99\xdc\xe4%f\xff\xf2\xffa_\xda\xec\xa4\x7f\xe3\x92\x00\x00\x00\x00\
IEND\xaeB`\x82\x98&j\xc6'
