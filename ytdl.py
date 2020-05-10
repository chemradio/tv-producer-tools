from __future__ import unicode_literals
import youtube_dl
from operator import itemgetter
from pprint import pprint


class YtdlEngine():
    ydl_opts = {
        'nocheckcertificate': True,
        # 'forcejson': True,
        'format': 'best',
        'simulate': True,
        'skip_download': True,
        'playlistend': 1
    }
    ydl = youtube_dl.YoutubeDL(ydl_opts)

    def go_ahead(self, url, verbose=False):
        if 'youtube' in url or 'youtu.be' in url:
            islist = url.find('&list')
            if islist == -1:
                url = url
            else:
                url = url[:islist]

        best_muxed_dict = {}
        list_formats = []
        ytdl_dict = {}
        ytdl_dict = self.ydl.extract_info(url=url, download=False)

        ytdl_formats = ytdl_dict['formats']
        if verbose == True:
            pprint(ytdl_dict)
            pprint(ytdl_formats)

        if 'youtube' in ytdl_dict['extractor']:
            for item in ytdl_formats:
                one_file = {}
                if item['ext'] == 'mp4':

                    if 'acodec' in item and item['acodec'] != 'none'.casefold():
                        one_file['Audio'] = 'Yes'
                    else:
                        one_file['Audio'] = 'No'

                    if 'width' and 'height' in item:
                        one_file['Resolution'] = f'{item["width"]} x {item["height"]}'
                        one_file['Pixels'] = int(item["width"]) * int(item["height"])
                    else:
                        one_file['Pixels'] = 0
                    one_file['URL'] = item['url']
                    one_file['Uploader'] = ytdl_dict['uploader']
                    list_formats.append(one_file)
                else:
                    continue

        elif ytdl_dict['extractor'] == 'facebook':
            for item in ytdl_formats:
                if item['ext'] == 'mp4':
                    one_file = {'Audio': 'Probably'}
                    if 'width' and 'height' in item:
                        one_file['Resolution'] = f'{item["width"]} x {item["height"]}'
                        one_file['Pixels'] = int(item["width"]) * int(item["height"])
                    elif 'format' in item and 'dash_hd_src' in item['format']:
                        one_file['Resolution'] = 'HD'
                        one_file['Pixels'] = 2073600
                    elif 'format' in item and 'dash_sd_src' in item['format']:
                        one_file['Resolution'] = 'SD'
                        one_file['Pixels'] = 2073599
                    else:
                        one_file['Pixels'] = 0
                    one_file['URL'] = item['url']
                    one_file['Uploader'] = ytdl_dict['uploader']
                    list_formats.append(one_file)
                else:
                    continue

        elif ytdl_dict['extractor'] == 'Instagram':
            for item in ytdl_formats:
                one_file = {}
                if item['ext'] == 'mp4':
                    one_file['Audio'] = 'Probably'

                    if 'width' and 'height' in item:
                        one_file['Resolution'] = f'{item["width"]} x {item["height"]}'
                        one_file['Pixels'] = int(item["width"]) * int(item["height"])
                    else:
                        one_file['Resolution'] = 'Unknown'
                        one_file['Pixels'] = 0
                    one_file['URL'] = item['url']
                    one_file['Uploader'] = ytdl_dict['uploader_id']
                    list_formats.append(one_file)
                else:
                    continue

        elif ytdl_dict['extractor'] == 'twitter':
            for item in ytdl_formats:
                if item['ext'] == 'mp4' and 'http' in item['protocol']:
                    one_file = {'Audio': 'Probably'}

                    if 'width' and 'height' in item:
                        one_file['Resolution'] = f'{item["width"]} x {item["height"]}'
                        one_file['Pixels'] = int(item["width"]) * int(item["height"])
                    else:
                        one_file['Resolution'] = 'Unknown'
                        one_file['Pixels'] = 0
                    one_file['URL'] = item['url']
                    one_file['Uploader'] = ytdl_dict['uploader_id']
                    list_formats.append(one_file)
                else:
                    continue

        else:
            for item in ytdl_formats:
                one_file = {'Audio': 'Probably'}
                if 'width' and 'height' in item:
                    one_file['Resolution'] = f'{item["width"]} x {item["height"]}'
                    one_file['Pixels'] = int(item["width"]) * int(item["height"])
                else:
                    one_file['Resolution'] = 'Unknown'
                    one_file['Pixels'] = 0
                one_file['URL'] = item['url']
                if 'uploader_id' in one_file['Uploader']:
                    one_file['Uploader'] = ytdl_dict['uploader_id']
                elif 'uploader' in one_file['Uploader']:
                    one_file['Uploader'] = ytdl_dict['uploader']
                else:
                    one_file['Uploader'] = 'unknown'
                list_formats.append(one_file)

        list_formats.sort(key=itemgetter('Pixels'), reverse=True)
        best_video_dict = list_formats[0]
        for item in list_formats:
            if item['Audio'] != 'No':
                best_muxed_dict = item
                break

        # pprint(best_muxed_dict)
        # pprint(best_video_dict)

        best_muxed_url = best_muxed_dict['URL']
        best_video_url = best_video_dict['URL']
        host = ytdl_dict['extractor_key']
        uploader = best_muxed_dict['Uploader']
        muxed_resolution = best_muxed_dict['Resolution']
        best_resolution = best_video_dict['Resolution']



        if best_muxed_dict == best_video_dict or 'Pixels' in best_muxed_dict and 'Pixels' in best_video_dict and best_muxed_dict['Pixels'] == best_video_dict['Pixels']:
            return False, host, uploader, muxed_resolution, best_muxed_url, 1, 1
        else:
            return True, host, uploader, muxed_resolution, best_muxed_url, best_resolution, best_video_url
