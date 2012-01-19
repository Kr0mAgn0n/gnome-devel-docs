require 'rubypants'

class Typography < RubyPants

    def to_html
        # Parse the HTML
        tokens = tokenize

        # Keep track of when we're inside <pre> or <code> tags.
        in_pre = false

        # Here is the result stored in.
        result = ""

        # This is a cheat, used to get some context for one-character
        # tokens that consist of just a quote char. What we do is remember
        # the last character of the previous text token, to use as context
        # to curl single- character quote tokens correctly.
        prev_token_last_char = nil

        tokens.each { |token|
            if token.first == :tag
                result << token[1]
                if token[1] =~ %r!<(/?)(?:pre|code|kbd|script|math)[\s>]!
                    in_pre = ($1 != "/")  # Opening or closing tag?
                end
            else
                t = token[1]

                # Remember last char of this token before processing.
                last_char = t[-1].chr

                unless in_pre
                    t = process_escapes t

                    t.gsub!(/&quot;/, '"')

                    t = educate_dashes t
                    t = educate_dashes_oldschool t
                    t = educate_dashes_inverted t

                    t = educate_ellipses t

                    # Note: backticks need to be processed before quotes.
                    t = educate_backticks t
                    t = educate_single_backticks t

                    if t == "'"
                        # Special case: single-character ' token
                        if prev_token_last_char =~ /\S/
                            t = "&#8217;"
                        else
                            t = "&#8216;"
                        end
                    elsif t == '"'
                        # Special case: single-character " token
                        if prev_token_last_char =~ /\S/
                            t = "&#8221;"
                        else
                            t = "&#8220;"
                        end
                    else
                        # Normal case:
                        t = educate_quotes t
                    end

                    t = stupefy_entities t
                end

                prev_token_last_char = last_char
                result << t
            end
        }

        # Done
        gnome widows(result)
    end

    protected

    def gnome(text)
        text.gsub(/(GNOME(\s+3)?)/,'<span class="gnome">\1</span>')
    end

    def widows(text)
        text.gsub(/(\s+)((<[^>]+>\s*)?[^<>\s]+(<\/(a|em|span|strong)[^>]*>\s*)*(<\/(p|h[1-6]|li|dt|dd)|$))/, '&nbsp;\2')
    end
end

module Haml::Helpers
#    include Haml::Filters::Base

    def typography(&block)
        text = capture_haml(&block)
        Typography.new(text).to_html
    end
end
