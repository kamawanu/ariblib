#!/usr/bin/env python3.2
# coding: utf-8

"""定数定義"""

# ARIB-STD-B10-2-H コンテント記述子におけるジャンル指定
CONTENT_TYPE = {
    0x0: ('ニュース／報道', {
        0x0: '定時・総合',
        0x1: '天気',
        0x2: '特集・ドキュメント',
        0x3: '政治・国会',
        0x4: '経済・市況',
        0x5: '海外・国際',
        0x6: '解説',
        0x7: '討論・会談',
        0x8: '報道特番',
        0x9: 'ローカル・地域',
        0xA: '交通',
        0xF: 'その他',
    }),
    0x1: ('スポーツ', {
        0x0: 'スポーツニュース',
        0x1: '野球',
        0x2: 'サッカー',
        0x3: 'ゴルフ',
        0x4: 'その他の球技',
        0x5: '相撲・格闘技',
        0x6: 'オリンピック・国際大会',
        0x7: 'マラソン・陸上・水泳',
        0x8: 'モータースポーツ',
        0x9: 'マリン・ウィンタースポーツ',
        0xA: '競馬・公営競技',
        0xF: 'その他',
    }),
    0x2: ('情報／ワイドショー', {
        0x0: '芸能・ワイドショー',
        0x1: 'ファッション',
        0x2: '暮らし・住まい',
        0x3: '健康・医療',
        0x4: 'ショッピング・通販',
        0x5: 'グルメ・料理',
        0x6: 'イベント',
        0x7: '番組紹介・お知らせ',
        0xF: 'その他',
    }),
    0x3: ('ドラマ', {
        0x0: '国内ドラマ',
        0x1: '海外ドラマ',
        0x2: '時代劇',
        0xF: 'その他',
    }),
    0x4: ('音楽', {
        0x0: '国内ロック・ポップス',
        0x1: '海外ロック・ポップス',
        0x2: 'クラシック・オペラ',
        0x3: 'ジャズ・フュージョン',
        0x4: '歌謡曲・演歌',
        0x5: 'ライブ・コンサート',
        0x6: 'ランキング・リクエスト',
        0x7: 'カラオケ・のど自慢',
        0x8: '民謡・邦楽',
        0x9: '童謡・キッズ',
        0xA: '民族音楽・ワールドミュージック',
        0xF: 'その他',
    }),
    0x5: ('バラエティ', {
        0x0: 'クイズ',
        0x1: 'ゲーム',
        0x2: 'トークバラエティ',
        0x3: 'お笑い・コメディ',
        0x4: '音楽バラエティ',
        0x5: '旅バラエティ',
        0x6: '料理バラエティ',
        0xF: 'その他',
    }),
    0x6: ('映画', {
        0x0: '洋画',
        0x1: '邦画',
        0x2: 'アニメ',
        0xF: 'その他',
    }),
    0x7: ('アニメ／特撮', {
        0x0: '国内アニメ',
        0x1: '海外アニメ',
        0x2: '特撮',
        0xF: 'その他',
    }),
    0x8: ('ドキュメンタリー／教養', {
        0x0: '社会・時事',
        0x1: '歴史・紀行',
        0x2: '自然・動物・環境',
        0x3: '宇宙・科学・医学',
        0x4: 'カルチャー・伝統文化',
        0x5: '文学・文芸',
        0x6: 'スポーツ',
        0x7: 'ドキュメンタリー全般',
        0x8: 'インタビュー・討論',
        0xF: 'その他',
    }),
    0x9: ('劇場／公演', {
        0x0: '現代劇・新劇',
        0x1: 'ミュージカル',
        0x2: 'ダンス・バレエ',
        0x3: '落語・演芸',
        0x4: '歌舞伎・古典',
        0xF: 'その他',
    }),
    0xA: ('趣味／教育', {
        0x0: '旅・釣り・アウトドア',
        0x1: '園芸・ペット・手芸',
        0x2: '音楽・美術・工芸',
        0x3: '囲碁・将棋',
        0x4: '麻雀・パチンコ',
        0x5: '車・オートバイ',
        0x6: 'コンピュータ・ＴＶゲーム',
        0x7: '会話・語学',
        0x8: '幼児・小学生',
        0x9: '中学生・高校生',
        0xA: '大学生・受験',
        0xB: '生涯教育・資格',
        0xC: '教育問題',
        0xF: 'その他',
    }),
    0xB: ('福祉', {
        0x0: '高齢者',
        0x1: '障害者',
        0x2: '社会福祉',
        0x3: 'ボランティア',
        0x4: '手話',
        0x5: '文字（字幕）',
        0x6: '音声解説',
        0xF: 'その他',
    }),
    0xE: ('拡張', {
        0x0: 'BS/地上デジタル放送用番組付属情報',
        0x1: '広帯域CS デジタル放送用拡張',
        0x2: '衛星デジタル音声放送用拡張',
        0x3: 'サーバー型番組付属情報',
        0x4: 'IP 放送用番組付属情報',
    }),
    0xF: ('その他',{
        0xF: 'その他',
    }),
}

# ARIB-STD-B10-2-6.2.3 表6-5 コンポーネント内容とコンポーネント種別
COMPONENT_TYPE = {
    0x01: {
        0x00: '将来使用のためリザーブ',
        0x01: '映像480i(525i)、アスペクト比4:3',
        0x02: '映像480i(525i)、アスペクト比16:9 パンベクトルあり',
        0x03: '映像480i(525i)、アスペクト比16:9 パンベクトルなし',
        0x04: '映像480i(525i)、アスペクト比16:9',
        0x91: '映像2160p、アスペクト比4:3',
        0x92: '映像2160p、アスペクト比16:9 パンベクトルあり',
        0x93: '映像2160p、アスペクト比16:9 パンベクトルなし',
        0x94: '映像2160p、アスペクト比16:9',
        0xA1: '映像480p(525p)、アスペクト比4:3',
        0xA2: '映像480p(525p)、アスペクト比16:9 パンベクトルあり',
        0xA3: '映像480p(525p)、アスペクト比16:9 パンベクトルなし',
        0xA4: '映像480p(525p)、アスペクト比16:9',
        0xB1: '映像1080i(1125i)、アスペクト比4:3',
        0xB2: '映像1080i(1125i)、アスペクト比16:9 パンベクトルあり',
        0xB3: '映像1080i(1125i)、アスペクト比16:9 パンベクトルなし',
        0xB4: '映像1080i(1125i)、アスペクト比16:9',
        0xC1: '映像720p(750p)、アスペクト比4:3',
        0xC2: '映像720p(750p)、アスペクト比16:9 パンベクトルあり',
        0xC3: '映像720p(750p)、アスペクト比16:9 パンベクトルなし',
        0xC4: '映像720p(750p)、アスペクト比16:9',
        0xD1: '映像240p アスペクト比4:3',
        0xD2: '映像240p アスペクト比16:9 パンベクトルあり',
        0xD3: '映像240p アスペクト比16:9 パンベクトルなし',
        0xD4: '映像240p アスペクト比16:9',
        0xE1: '映像1080p(1125p)、アスペクト比4:3',
        0xE2: '映像1080p(1125p)、アスペクト比16:9 パンベクトルあり',
        0xE3: '映像1080p(1125p)、アスペクト比16:9 パンベクトルなし',
        0xE4: '映像1080p(1125p)、アスペクト比16:9',
        0xF1: '映像180p アスペクト比4:3',
        0xF2: '映像180p アスペクト比16:9 パンベクトルあり',
        0xF3: '映像180p アスペクト比16:9 パンベクトルなし',
        0xF4: '映像180p アスペクト比16:9',
    },
    0x02: {
        0x00: '将来使用のためリザーブ',
        0x01: '1/0モード(シングルモノ)',
        0x02: '1/0+1/0モード(デュアルモノ)',
        0x03: '2/0モード(ステレオ)',
        0x04: '2/1モード',
        0x05: '3/0モード',
        0x06: '2/2モード',
        0x07: '3/1モード',
        0x08: '3/2モード',
        0x09: '3/2+LFEモード(3/2.1モード)',
        0x0A: '3/3.1モード',
        0x0B: '2/0/0-2/0/2-0.1モード',
        0x0C: '5/2.1モード',
        0x0D: '3/2/2.1モード',
        0x0E: '2/0/0-3/0/2-0.1モード',
        0x0F: '0/2/0-3/0/2-0.2モード',
        0x10: '2/0/0-3/2/3-0.2モード',
        0x11: '3/3/3-5/2/3-3/0/0.2モード',
        0x40: '視覚障害者用音声解説',
        0x41: '聴覚障害者用音声',
    },
    0x05: {
        0x01: 'H.264|MPEG-4 AVC、 映像480i(525i)、アスペクト比4:3', 
        0x02: 'H.264|MPEG-4 AVC、 映像480i(525i)、アスペクト比16:9 パンベクトルあり',
        0x03: 'H.264|MPEG-4 AVC、 映像480i(525i)、アスペクト比16:9 パンベクトルなし ',
        0x04: 'H.264|MPEG-4 AVC、 映像480i(525i)、アスペクト比 > 16:9',
        0x91: 'H.264|MPEG-4 AVC、 映像2160p、アスペクト比4:3',
        0x92: 'H.264|MPEG-4 AVC、 映像2160p、アスペクト比16:9 パンベクトルあり',
        0x93: 'H.264|MPEG-4 AVC、 映像2160p、アスペクト比16:9 パンベクトルなし',
        0x94: 'H.264|MPEG-4 AVC、 映像2160p、アスペクト比 > 16:9',
        0xA1: 'H.264|MPEG-4 AVC、 映像480p(525p)、アスペクト比4:3',
        0xA2: 'H.264|MPEG-4 AVC、 映像480p(525p)、アスペクト比16:9 パンベクトルあり',
        0xA3: 'H.264|MPEG-4 AVC、 映像480p(525p)、アスペクト比16:9 パンベクトルなし',
        0xA4: 'H.264|MPEG-4 AVC、 映像480p(525p)、アスペクト比 > 16:9',
        0xB1: 'H.264|MPEG-4 AVC、 映像1080i(1125i)、アスペクト比4:3',
        0xB2: 'H.264|MPEG-4 AVC、 映像1080i(1125i)、アスペクト比16:9 パンベクトルあり',
        0xB3: 'H.264|MPEG-4 AVC、 映像1080i(1125i)、アスペクト比16:9 パンベクトルなし',
        0xB4: 'H.264|MPEG-4 AVC、 映像1080i(1125i)、アスペクト比 > 16:9',
        0xC1: 'H.264|MPEG-4 AVC、 映像720p(750p)、アスペクト比4:3',
        0xC2: 'H.264|MPEG-4 AVC、 映像720p(750p)、アスペクト比16:9 パンベクトルあり',
        0xC3: 'H.264|MPEG-4 AVC、 映像720p(750p)、アスペクト比16:9 パンベクトルなし',
        0xC4: 'H.264|MPEG-4 AVC、 映像720p(750p)、アスペクト比 > 16:9',
        0xD1: 'H.264|MPEG-4 AVC、 映像240p アスペクト比4:3',
        0xD2: 'H.264|MPEG-4 AVC、 映像240p アスペクト比16:9 パンベクトルあり',
        0xD3: 'H.264|MPEG-4 AVC、 映像240p アスペクト比16:9 パンベクトルなし',
        0xD4: 'H.264|MPEG-4 AVC、 映像240p アスペクト比 > 16:9',
        0xE1: 'H.264|MPEG-4 AVC、 映像1080p(1125p)、アスペクト比4:3',
        0xE2: 'H.264|MPEG-4 AVC、 映像1080p(1125p)、アスペクト比16:9 パンベクトルあり',
        0xE3: 'H.264|MPEG-4 AVC、 映像1080p(1125p)、アスペクト比16:9 パンベクトルなし',
        0xE4: 'H.264|MPEG-4 AVC、 映像1080p(1125p)、アスペクト比 > 16:9',
        0xF1: 'H.264|MPEG-4 AVC、 映像180p アスペクト比4:3',
        0xF2: 'H.264|MPEG-4 AVC、 映像180p アスペクト比16:9 パンベクトルあり',
        0xF3: 'H.264|MPEG-4 AVC、 映像180p アスペクト比16:9 パンベクトルなし',
        0xF4: 'H.264|MPEG-4 AVC、 映像180p アスペクト比 > 16:9',
    },
}

# ARIB-STD-B10-2-6.2.26 表6-44 音質表示
QUOLITY = {
    0b00: '将来使用のためリザーブ',
    0b01: 'モード1',
    0b10: 'モード2',
    0b11: 'モード3',
}

# ARIB-STD-B10-2-6.2.26 表6-45 サンプリング周波数
SAMPLING_RATE = {
    0b000: '将来使用のためリザーブ',
    0b001: '16kHz',
    0b010: '22.05kHz',
    0b011: '24kHz',
    0b100: 'リザーブ',
    0b101: '32kHz',
    0b110: '44.1kHz',
    0b111: '48kHz'
}

# ARIB-STD-B10-2-6.2.13 表6-25 サービス形式種別
SERVICE_TYPES = {
    0x00: '未定義',
    0x01: 'デジタルTVサービス',
    0x02: 'デジタル音声サービス',
    0xA1: '臨時映像サービス',
    0xA2: '臨時音声サービス',
    0xA3: '臨時データサービス',
    0xA4: 'エンジニアリングサービス',
    0xA5: 'プロモーション映像サービス',
    0xA6: 'プロモーション音声サービス',
    0xA7: 'プロモーションデータサービス',
    0xA8: '事前蓄積用データサービス',
    0xA9: '蓄積専用データサービス',
    0xAA: 'ブックマーク一覧データサービス',
    0xAB: 'サーバー型サイマルサービス',
    0xAC: '独立ファイルサービス',
    0xC0: 'データサービス',
    0xC1: 'TLVを用いた蓄積型サービス',
    0xC2: 'マルチメディアサービス',
}

# ARIB-STD-B1aS0-2-6.2.8 表6-14 リンク種別のコード
LINKAGE_TYPES = {
    0x01: '情報サービス',
    0x02: '電子番組ガイド(EPG)サービス',
    0x03: 'CA代替サービス',
    0x04: '全てのネットワーク/ブーケSIを含むトランスポートストリーム',
    0x05: '代替サービス',
    0x06: 'データ放送サービス',
    0x0B: 'INT',
    0xFE: '再送信用',
}

# ARIB-STD-B10-2-6.2.23 表6-39 デジタルコピー制御情報
DIGITAL_RECORDING_CONTROL_TYPE = {
    0b00: '制約条件なしにコピー可',
    0b01: 'コピー禁止',
    0b10: '1世代のみコピー可',
    0b11: 'コピー禁止',
}

# ARIB-STD-B10-2-6.2.34 表6-68 グループ種別
EVENT_GROUP_TYPE = {
    0x00: '未定義',
    0x01: 'イベント共有',
    0x02: 'イベントリレー',
    0x03: 'イベント移動',
    0x04: '他ネットワークへのイベントリレー',
    0x05: '他ネットワークからのイベント移動',
}

# ISO 13818-1 2.4.4.10 Table 2-29 Stream type assignments
STREAM_TYPE = {
    0x00: 'ITU-T | ISO/IEC Reserved',
    0x01: 'ISO/IEC 11172 Video',
    0x02: ('ITU-T Rec. H.262 | ISO/IEC 13818-2 Video or ISO/IEC 11172-2 '
           'constrained parameter video stream'),
    0x03: 'ISO/IEC 11172 Audio',
    0x04: 'ISO/IEC 13818-3 Audio',
    0x05: 'ITU-T Rec. H.222.0 | ISO/IEC 13818-1 private_sections',
    0x06: 'ITU-T Rec. H.222.0 | ISO/IEC 13818-1 PES packets containing private data',
    0x07: 'ISO/IEC 13522 MHEG',
    0x08: 'ITU-T Rec. H.222.0 | ISO/IEC 13818-1 Annex A DSM-CC',
    0x09: 'ITU-T Rec. H.222.1',
    0x0A: 'ISO/IEC 13818-6 type A',
    0x0B: 'ISO/IEC 13818-6 type B',
    0x0C: 'ISO/IEC 13818-6 type C',
    0x0D: 'ISO/IEC 13818-6 type D',
    0x0E: 'ITU-T Rec. H.222.0 | ISO/IEC 13818-1 auxiliary',
    0x0F: 'ISO/IEC 13818-7 Audio with ADTS transport syntax',
    0x10: 'ISO/IEC 14496-2 Visual',
    0x11: ('ISO/IEC 14496-3 Audio with the LATM transport syntax as defined '
           'in ISO/IEC 14496-3 / AMD 1'),
    0x12: ('ISO/IEC 14496-1 SL-packetized stream or FlexMux stream carried '
           'in PES packets'),
    0x13: ('ISO/IEC 14496-1 SL-packetized stream or FlexMux stream carried '
           'in ISO/IEC14496_sections.'),
    0x14: 'ISO/IEC 13818-6 Synchronized Download Protocol',
}

# ARIB-STD-B10-2-D 表D-2 地域符号
AREA_CODES = {
    0b101001011010: '静岡県',
    0b100101100110: '愛知県',
    0b001011011100: '三重県',
    0b110011100100: '滋賀県',
    0b010110011010: '京都府',
    0b110010110010: '大阪府',
    0b011001110100: '兵庫県',
    0b101010010011: '奈良県',
    0b001110010110: '和歌山県',
    0b110100100011: '鳥取県',
    0b001100011011: '島根県',
    0b001010110101: '岡山県',
    0b101100110001: '広島県',
    0b101110011000: '山口県',
    0b111001100010: '徳島県',
    0b100110110100: '香川県',
    0b000110011101: '愛媛県',
    0b001011100011: '高知県',
    0b011000101101: '福岡県',
    0b100101011001: '佐賀県',
    0b101000101011: '長崎県',
    0b100010100111: '熊本県',
    0b110010001101: '大分県',
    0b110100011100: '宮崎県',
    0b110101000101: '鹿児島県',
    0b001101110010: '沖縄県',
    0b001101001101: '地域共通',
    0b010110100101: '関東広域圏',
    0b011100101010: '中京広域圏',
    0b100011010101: '近畿広域圏',
    0b011010011001: '鳥取・島根圏',
    0b010101010011: '岡山・香川圏',
    0b000101101011: '北海道',
    0b010001100111: '青森県',
    0b010111010100: '岩手県',
    0b011101011000: '宮城県',
    0b101011000110: '秋田県',
    0b111001001100: '山形県',
    0b000110101110: '福島県',
    0b110001101001: '茨城県',
    0b111000111000: '栃木県',
    0b100110001011: '群馬県',
    0b011001001011: '埼玉県',
    0b000111000111: '千葉県',
    0b101010101100: '東京都',
    0b010101101100: '神奈川県',
    0b010011001110: '新潟県',
    0b010100111001: '富山県',
    0b011010100110: '石川県',
    0b100100101101: '福井県',
    0b110101001010: '山梨県',
    0b100111010010: '長野県',
    0b101001100101: '岐阜県',
}

# ARIB-STD-B10-2-6.2.30 表6-60 ビデオエンコードフォーマット
VIDEO_ENCODE_FORMATS = {
    0b0000: '1080p',
    0b0001: '1080i',
    0b0010: '720p',
    0b0011: '480p',
    0b0100: '480i',
    0b0101: '240o',
    0b0110: '120p',
    0b0111: '2160p',
    0b1000: '180p',
}